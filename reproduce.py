"""Reproduce the existing six-fund result; this is not a Lab 20 changed-input run."""
from pathlib import Path
import json
import portfolio

ROOT = Path(__file__).resolve().parent


def main():
    estimates = portfolio.estimate_from_csv(ROOT / "prices.csv")
    result = portfolio.search_lowest_risk(
        estimates["assets"], estimates["correlations"], 0.06, 0.05, ["BIL"]
    )
    if result is None:
        raise SystemExit("No feasible mix under the existing exercise settings.")
    record = {
        "scope": "Existing Lab 15 six-fund exercise, not an approved Project 2 mandate",
        "objective_gross": 0.06,
        "reserve_minimum": 0.05,
        "estimates": estimates,
        "result": result,
    }
    output = ROOT / "outputs"
    output.mkdir(exist_ok=True)
    (output / "baseline.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    rows = "\n".join(f"| {name} | {weight:.2%} |" for name, weight in result["weights"].items())
    report = (
        "# Existing six-fund result\n\n"
        "AI-assisted reproduction. Education, not investment advice.\n\n"
        "This reproduces the Lab 15 exercise. It does not establish readiness under the full Project 2 mandate.\n\n"
        f"Prices: {estimates['price_start']} through {estimates['price_end']}; "
        f"{estimates['return_months']} monthly returns.\n\n"
        "Settings: minimize estimated volatility on a 5-percentage-point grid; "
        "at least 6% gross estimated annual return; at least 5% BIL; long-only; fully invested.\n\n"
        f"| Asset | Weight |\n|---|---:|\n{rows}\n\n"
        f"Estimated annual gross return: **{result['return']:.2%}**.\n\n"
        f"Estimated annual volatility: **{result['volatility']:.2%}**.\n\n"
        f"Reserve-eligible weight: **{result['reserve_weight']:.2%}**.\n\n"
        "Exercise screen: **PASS**. Full Project 2 mandate: **NOT ESTABLISHED**.\n\n"
        "Historical arithmetic estimates are not forecasts or out-of-sample results. "
        "Costs and taxes are excluded. This is a baseline reproduction, not the AI-off changed-input exercise.\n"
    )
    (output / "baseline.md").write_text(report, encoding="utf-8")
    print(report)
    print("Saved outputs/baseline.md and outputs/baseline.json")


if __name__ == "__main__":
    main()
