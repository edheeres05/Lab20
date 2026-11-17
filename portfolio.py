"""FIN 439 Lab 14: Meridian portfolio baselines (standard-library only).

Course-provided hypothetical annual return, volatility, and correlation inputs.
All percentages are stored as decimals. This file can be imported by Thursday's app.
"""

from math import isclose, isfinite, sqrt

# Editable inputs: order matters for the correlation rows/columns.
ASSETS = {
    "Treasury bills": {"return": 0.035, "volatility": 0.005},
    "Treasury 10-year note": {"return": 0.043, "volatility": 0.070},
    "Investment-grade bond fund": {"return": 0.050, "volatility": 0.060},
    "Global equity index fund": {"return": 0.080, "volatility": 0.160},
}

# Rows and columns: bills, 10-year Treasury, IG bonds, equity.
CORRELATIONS = [
    [1.00, 0.10, 0.05, 0.00],
    [0.10, 1.00, 0.80, -0.10],
    [0.05, 0.80, 1.00, 0.25],
    [0.00, -0.10, 0.25, 1.00],
]

ESTIMATED_CPI = 0.025
RETURN_ABOVE_CPI = 0.040
OBJECTIVE_RETURN = ESTIMATED_CPI + RETURN_ABOVE_CPI  # 6.5%
RESERVE_ASSETS = ("Treasury bills", "Treasury 10-year note")


def validate_inputs(assets=ASSETS, correlations=CORRELATIONS):
    """Stop with a clear error if volatility/correlation inputs are invalid."""
    names = list(assets)
    n = len(names)
    if n == 0 or len(correlations) != n or any(len(row) != n for row in correlations):
        raise ValueError("Correlation table must be square and match the asset list.")

    for name, values in assets.items():
        for field in ("return", "volatility"):
            if not isfinite(values[field]):
                raise ValueError(f"{name}: {field} must be a finite number.")
        if values["volatility"] <= 0:
            raise ValueError(f"{name}: volatility must be greater than zero.")

    for i in range(n):
        for j in range(n):
            correlation = correlations[i][j]
            if not isfinite(correlation) or correlation < -1 or correlation > 1:
                raise ValueError(
                    f"Invalid correlation {correlation} for {names[i]} and {names[j]}; "
                    "correlations must be between -1 and 1."
                )
            if not isclose(correlation, correlations[j][i], abs_tol=1e-12):
                raise ValueError(
                    f"Correlation table is not symmetric for {names[i]} and {names[j]}."
                )
        if not isclose(correlations[i][i], 1.0, abs_tol=1e-12):
            raise ValueError(f"Self-correlation must be 1 for {names[i]}.")


def make_covariance_matrix(assets=ASSETS, correlations=CORRELATIONS):
    """Covariance = correlation × volatility of asset i × volatility of asset j."""
    validate_inputs(assets, correlations)
    names = list(assets)
    return [
        [
            correlations[i][j]
            * assets[names[i]]["volatility"]
            * assets[names[j]]["volatility"]
            for j in range(len(names))
        ]
        for i in range(len(names))
    ]


def benchmark_weights(assets=ASSETS):
    """Meridian's 40% IG bond / 60% global equity comparison benchmark."""
    return {
        name: (
            0.40 if name == "Investment-grade bond fund" else
            0.60 if name == "Global equity index fund" else 0.0
        )
        for name in assets
    }


def equal_weights(assets=ASSETS):
    """Each asset receives an equal share."""
    return {name: 1 / len(assets) for name in assets}


def inverse_volatility_weights(assets=ASSETS):
    """Lower standalone volatility produces a larger weight."""
    inverses = {name: 1 / values["volatility"] for name, values in assets.items()}
    total = sum(inverses.values())
    return {name: inverse / total for name, inverse in inverses.items()}


def validate_weights(weights, assets=ASSETS):
    if set(weights) != set(assets):
        raise ValueError("Portfolio weights must cover the exact asset list.")
    if any(not isfinite(weight) or weight < 0 for weight in weights.values()):
        raise ValueError("Portfolio weights must be finite and nonnegative.")
    if not isclose(sum(weights.values()), 1.0, abs_tol=1e-10):
        raise ValueError("Portfolio weights must add to 100%.")


def expected_return(weights, assets=ASSETS):
    """Sum(weight × annual expected return) for every asset."""
    validate_weights(weights, assets)
    return sum(weights[name] * values["return"] for name, values in assets.items())


def portfolio_variance(weights, covariance, assets=ASSETS):
    """Sum(w_i × w_j × covariance_ij) across *all* pairs of assets."""
    validate_weights(weights, assets)
    names = list(assets)
    return sum(
        weights[names[i]] * weights[names[j]] * covariance[i][j]
        for i in range(len(names))
        for j in range(len(names))
    )


def portfolio_volatility(weights, covariance, assets=ASSETS):
    """Portfolio volatility is the square root of portfolio variance."""
    variance = portfolio_variance(weights, covariance, assets)
    if variance < -1e-12:
        raise ValueError("Negative portfolio variance: check the correlation matrix.")
    return sqrt(max(variance, 0.0))


def reserve_weight(weights):
    """Only Treasury bills and Treasury 10-year notes are eligible in this lab."""
    return sum(weights.get(name, 0.0) for name in RESERVE_ASSETS)


def meets_objective(annual_expected_return, objective=OBJECTIVE_RETURN):
    return annual_expected_return >= objective


def main():
    cov = make_covariance_matrix()
    portfolios = {
        "Benchmark": benchmark_weights(),
        "Equal weight": equal_weights(),
        "Inverse volatility": inverse_volatility_weights(),
    }
    print("Meridian course training inputs (not market forecasts)")
    print(f"Estimated objective: CPI {ESTIMATED_CPI:.1%} + 4.0% = {OBJECTIVE_RETURN:.1%}")
    print("Weights: bills / 10-year / IG bonds / equity")
    for name, weights in portfolios.items():
        ret = expected_return(weights)
        vol = portfolio_volatility(weights, cov)
        print(f"\n{name}")
        print("Weights (%): " + " / ".join(f"{100 * w:.1f}" for w in weights.values()))
        print(f"Expected return: {ret:.2%}")
        print(f"Volatility: {vol:.2%}")
        print(f"Reserve-eligible: {reserve_weight(weights):.1%}")
        print(f"Meets {OBJECTIVE_RETURN:.1%} return objective: {'yes' if meets_objective(ret) else 'no'}")


def search_lowest_risk(assets=ASSETS, correlations=CORRELATIONS,
                       objective=OBJECTIVE_RETURN, reserve_minimum=0.03,
                       reserve_assets=RESERVE_ASSETS):
    """Try every 5-percentage-point long-only mix; return the safest or None.

    Inputs/outputs are decimals (0.065 means 6.5%). This is a grid minimum,
    not a continuous optimizer. Ties keep the first mix in asset order.
    Only the return and reserve rules are screened here.
    """
    import numpy as np

    names = list(assets)
    if not 1 <= len(names) <= 6:
        raise ValueError("The search supports one to six assets.")
    if not isfinite(objective):
        raise ValueError("The objective must be finite.")
    if not isfinite(reserve_minimum) or not 0 <= reserve_minimum <= 1:
        raise ValueError("The reserve minimum must be between 0% and 100%.")
    eligible = set(reserve_assets)
    if not eligible.issubset(assets):
        raise ValueError("Every reserve-eligible asset must be in the universe.")
    covariance = make_covariance_matrix(assets, correlations)
    if np.linalg.eigvalsh(np.asarray(correlations)).min() < -1e-10:
        raise ValueError("The correlations do not form a valid joint risk matrix.")

    def mixes(units_left, assets_left):
        # 20 units divide 100% into 5-point pieces, with no rounding drift.
        if assets_left == 1:
            yield (units_left,)
        else:
            for units in range(units_left + 1):
                for rest in mixes(units_left - units, assets_left - 1):
                    yield (units,) + rest

    best = None
    for units in mixes(20, len(names)):
        weights = dict(zip(names, (unit / 20 for unit in units)))
        annual_return = expected_return(weights, assets)
        reserve = sum(weights[name] for name in eligible)
        if annual_return + 1e-12 < objective or reserve + 1e-12 < reserve_minimum:
            continue
        volatility = portfolio_volatility(weights, covariance, assets)
        if best is None or volatility < best["volatility"] - 1e-12:
            best = {"weights": weights, "return": annual_return,
                    "volatility": volatility, "reserve_weight": reserve}
    return best


def estimate_from_csv(csv_file, last_36=False):
    """Estimate from monthly adjusted-close prices; history, not a forecast.

    Date first, oldest first, one column per asset. No missing values are
    filled and no months are silently dropped. Last 36 means 36 RETURNS,
    which needs 37 price observations. Standard deviation uses ddof=1.
    Accepts a file path or a text/binary file-like object.
    """
    import csv
    from io import StringIO
    from pathlib import Path
    import numpy as np
    import pandas as pd

    raw = csv_file.read() if hasattr(csv_file, "read") else Path(csv_file).read_bytes()
    text = raw.decode("utf-8-sig") if isinstance(raw, bytes) else raw.lstrip("\ufeff")
    header = next(csv.reader(StringIO(text)), [])
    if len(header) < 4 or len(header) > 7:
        raise ValueError("CSV needs a date column followed by three to six assets.")
    if any(not name.strip() or name != name.strip() for name in header):
        raise ValueError("Column names must be nonblank and have no surrounding spaces.")
    if len({name.upper() for name in header}) != len(header):
        raise ValueError("CSV column names must be unique.")
    frame = pd.read_csv(StringIO(text))
    if len(frame) < 3:
        raise ValueError("At least three monthly price rows are needed.")
    dates = pd.to_datetime(frame.iloc[:, 0], format="%Y-%m-%d", errors="coerce")
    if dates.isna().any():
        raise ValueError("First column must contain dates in YYYY-MM-DD format.")
    if not dates.is_monotonic_increasing or dates.duplicated().any():
        raise ValueError("Dates must be unique and sorted oldest first.")
    months = dates.dt.to_period("M").astype("int64").to_numpy()
    if not (np.diff(months) == 1).all():
        raise ValueError("Use exactly one price row per consecutive month; a month is missing or repeated.")
    prices = frame.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")
    if not np.isfinite(prices.to_numpy()).all() or (prices <= 0).any().any():
        raise ValueError("Every adjusted close must be numeric, finite and positive; no blanks.")
    prices.index = pd.DatetimeIndex(dates)
    returns = prices.pct_change(fill_method=None).iloc[1:]
    if last_36:
        if len(returns) < 36:
            raise ValueError("Last 36 months requires at least 37 monthly price rows.")
        returns = returns.tail(36)
    annual_means = returns.mean() * 12
    annual_vols = returns.std(ddof=1) * sqrt(12)
    if (annual_vols <= 1e-12).any():
        raise ValueError("An asset has zero return volatility; its correlation cannot be estimated.")
    assets = {name: {"return": float(annual_means[name]),
                     "volatility": float(annual_vols[name])} for name in prices.columns}
    correlations = returns.corr().clip(-1, 1).to_numpy().tolist()
    validate_inputs(assets, correlations)
    return {"assets": assets, "correlations": correlations,
            "price_rows": len(prices), "return_months": len(returns),
            "price_start": prices.index[0].date().isoformat(),
            "price_end": prices.index[-1].date().isoformat(),
            "return_start": returns.index[0].date().isoformat(),
            "return_end": returns.index[-1].date().isoformat(),
            "estimate_label": "Annualized arithmetic historical mean; not a forecast; before trading costs."}


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"Input error: {error}")
