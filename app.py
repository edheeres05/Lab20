"""FIN 439 Lab 15. Run: py -m streamlit run app.py"""
from copy import deepcopy
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import importlib
import json

import pandas as pd
import streamlit as st
import portfolio

# Reload saved engine inputs when the page reruns, including the correlation probe.
engine = importlib.reload(portfolio)
st.set_page_config(page_title="Portfolio Stability Decision", page_icon="📊", layout="wide")
st.title("Portfolio Stability Decision")
st.caption("Built with AI help, a learning demonstration, not investment advice.")

st.sidebar.header("Data and mandate")
upload = st.sidebar.file_uploader("Upload prices.csv", type=["csv"])
bundled = st.sidebar.checkbox("Use included six-fund prices.csv", value=False)
last_36 = st.sidebar.toggle("Use only the last 36 monthly returns", value=False,
                            disabled=not (upload or bundled))
price_bytes = None
source_name = "Meridian training inputs"
if upload is not None:
    price_bytes = upload.getvalue()
    source_name = upload.name
elif bundled:
    price_path = Path(__file__).with_name("prices.csv")
    if not price_path.exists():
        st.error("prices.csv is missing. Upload your monthly adjusted-close CSV.")
        st.stop()
    price_bytes = price_path.read_bytes()
    source_name = "Included prices.csv: VOO, QQQ, SOXX, SCHD, BIL, BND"

try:
    if price_bytes is None:
        loaded_assets = deepcopy(engine.ASSETS)
        loaded_corr = deepcopy(engine.CORRELATIONS)
        current_assets, current_corr = deepcopy(loaded_assets), deepcopy(loaded_corr)
        base_meta = current_meta = None
        source_id = "Meridian:" + json.dumps([loaded_assets, loaded_corr])
        default_eligible = set(engine.RESERVE_ASSETS)
        window = "Course estimates"
    else:
        base_meta = engine.estimate_from_csv(BytesIO(price_bytes))
        current_meta = engine.estimate_from_csv(BytesIO(price_bytes), last_36=last_36)
        loaded_assets, loaded_corr = base_meta["assets"], base_meta["correlations"]
        current_assets, current_corr = deepcopy(current_meta["assets"]), current_meta["correlations"]
        source_id = sha256(price_bytes).hexdigest()
        default_eligible = {name for name in loaded_assets if name.upper() == "BIL"}
        window = "Last 36 monthly returns" if last_36 else "All monthly returns"
except (ValueError, UnicodeError, OSError, pd.errors.ParserError) as error:
    st.error(f"Cannot use this data: {error}")
    st.stop()

names = list(current_assets)
token = source_id + ":" + window
if st.session_state.get("source_id") != source_id:
    for i, name in enumerate(names):
        st.session_state[f"eligible_{i}"] = name in default_eligible
    st.session_state["source_id"] = source_id
if st.session_state.get("estimate_token") != token:
    for i, name in enumerate(names):
        st.session_state[f"return_{i}"] = current_assets[name]["return"] * 100
    st.session_state["estimate_token"] = token

if price_bytes is not None:
    if st.sidebar.button("Use proposed project settings: 6% / 5%"):
        st.session_state["objective_pct"] = 6.0
        st.session_state["reserve_pct"] = 5.0
        for i, name in enumerate(names):
            st.session_state[f"eligible_{i}"] = name.upper() == "BIL"
    st.sidebar.caption("From Lab 13/14: proposed 6% target, at least 5% BIL. This app screens gross historical estimates; it does not verify the full net-return mandate.")
else:
    if st.sidebar.button("Restore Meridian rules: 6.5% / 3%"):
        st.session_state["objective_pct"] = 6.5
        st.session_state["reserve_pct"] = 3.0
        for i, name in enumerate(names):
            st.session_state[f"eligible_{i}"] = name in default_eligible

st.session_state.setdefault("objective_pct", 6.5)
st.session_state.setdefault("reserve_pct", 3.0)
objective = st.sidebar.number_input("Expected return objective (%)",
                                     step=0.1, format="%.2f", key="objective_pct") / 100
reserve_min = st.sidebar.number_input("Minimum reserve weight (%)", min_value=0.0,
                                      max_value=100.0, step=1.0,
                                      format="%.2f", key="reserve_pct") / 100
st.sidebar.caption("Long-only. Weights sum to 100% in 5-point steps. A 3% reserve minimum therefore requires at least 5% on this grid.")

st.write(f"**Source:** {source_name}")
if current_meta:
    st.info("Return estimates are annualized arithmetic historical means, not forecasts. Trading costs and taxes are not deducted.")
    st.caption(f"{current_meta['price_rows']} prices, {current_meta['price_start']} to {current_meta['price_end']}. "
               f"Current estimate: {current_meta['return_months']} returns, "
               f"{current_meta['return_start']} to {current_meta['return_end']}. "
               f"As-loaded reference always uses all {base_meta['return_months']} returns.")
    if current_meta["price_rows"] not in (60, 61):
        st.warning("The lab asks for five years of monthly prices. Check the sample length before using these results.")
else:
    st.caption("Hypothetical annual course inputs. Bills and the 10-year note count as reserves under Meridian's rules.")

st.subheader("Edit the estimates")
st.caption("Change one expected return to stress the result. Switching data or time window reloads the return boxes. Both answers use the same selected objective and reserve rules.")
if st.button("Reset return estimates for this window"):
    for i, name in enumerate(names):
        st.session_state[f"return_{i}"] = current_assets[name]["return"] * 100
eligible = []
for start in range(0, len(names), 3):
    columns = st.columns(3)
    for offset, name in enumerate(names[start:start + 3]):
        i = start + offset
        with columns[offset]:
            current_assets[name]["return"] = st.number_input(
                f"{name} expected return (%)", step=0.1, format="%.2f", key=f"return_{i}") / 100
            if st.checkbox(f"{name}: reserve-eligible", key=f"eligible_{i}"):
                eligible.append(name)
            st.caption(f"Volatility: {100 * current_assets[name]['volatility']:.2f}%")

try:
    baseline = engine.search_lowest_risk(loaded_assets, loaded_corr, objective, reserve_min, eligible)
    scenario = engine.search_lowest_risk(current_assets, current_corr, objective, reserve_min, eligible)
except ValueError as error:
    st.error(f"Input error: {error}")
    st.stop()


def display_result(title, answer):
    st.subheader(title)
    if answer is None:
        st.warning("no mix meets the objective")
        st.caption("No 5-point mix satisfies both the return objective and reserve rule.")
        return
    st.dataframe(pd.DataFrame({"Asset": names, "Weight (%)": [round(100 * answer['weights'][n], 2) for n in names]}),
                 hide_index=True, width="stretch", column_config={"Weight (%)": st.column_config.NumberColumn(format="%.2f")})
    a, b = st.columns(2)
    a.metric("Expected annual return", f"{answer['return']:.2%}")
    b.metric("Annual volatility", f"{answer['volatility']:.2%}")
    st.metric("Reserve-eligible weight", f"{answer['reserve_weight']:.2%}")


left, right = st.columns(2)
with left:
    display_result("Current inputs: lowest-risk mix", scenario)
    st.caption(window + "; includes any return-box edits.")
with right:
    display_result("Inputs as loaded: reference mix", baseline)
    st.caption("Unedited returns and all-month risk estimates; same objective and reserve rules.")

largest = None
if baseline is not None and scenario is not None:
    changes = {name: 100 * abs(scenario['weights'][name] - baseline['weights'][name]) for name in names}
    largest = max(changes.values())
    st.metric("Largest weight change", f"{largest:.2f} percentage points")
    if largest > 1e-10:
        st.caption("Largest change in: " + ", ".join(n for n, v in changes.items() if abs(v - largest) < 1e-8))
else:
    st.info("Largest weight change: unavailable because at least one run has no feasible mix.")

with st.expander("Inspect assumptions and risk inputs"):
    st.write("This is the lowest volatility among feasible 5-point mixes, not an exact continuous optimum. Only long-only weights, full investment, the return objective and the selected reserve rule are enforced.")
    st.write("Project 2 still needs costs, timing, concentration, liquidity, turnover, benchmark and risk-policy checks. A displayed result is not approval under the complete mandate.")
    st.dataframe(pd.DataFrame(current_corr, index=names, columns=names).round(4))


def result_markdown(title, answer):
    if answer is None:
        return f"### {title}\n\nno mix meets the objective\n"
    rows = "\n".join(f"| {name} | {answer['weights'][name]:.2%} |" for name in names)
    return (f"### {title}\n\n| Asset | Weight |\n|---|---:|\n{rows}\n\n"
            f"Expected return: {answer['return']:.2%}; volatility: {answer['volatility']:.2%}; "
            f"reserve: {answer['reserve_weight']:.2%}.\n")


snapshot = ("# Lab 15 scenario snapshot\n\nBuilt with AI help; learning demonstration; not investment advice.\n\n"
            f"Source: {source_name}\n\nWindow: {window}\n\n"
            f"Objective: {objective:.2%}; minimum reserve: {reserve_min:.2%}; "
            f"eligible: {', '.join(eligible) or 'none'}.\n\n"
            + result_markdown("Inputs as loaded", baseline) + "\n"
            + result_markdown("Current inputs", scenario) + "\n"
            + (f"Largest weight change: {largest:.2f} percentage points.\n" if largest is not None else "Largest weight change: unavailable.\n")
            + "\n## Current annual return assumptions\n\n"
            + "\n".join(f"- {n}: {current_assets[n]['return']:.6%}" for n in names)
            + "\n\nHistorical estimates are not forecasts. Results are before trading costs and taxes.\n")
st.download_button("Download this comparison as Markdown", snapshot,
                   file_name="Lab15_scenario_snapshot.md", mime="text/markdown")
