# Price data sources

Retrieved October 22, 2026 with the supplied Lab 14 [build_prices.py](https://github.com/edheeres05/Lab15WebAPP/blob/main/build_prices.py).

Provider: Yahoo Finance chart JSON, `indicators.adjclose[0].adjclose` (not unadjusted close).

| Ticker | Historical-data page | Machine endpoint |
|---|---|---|
| VOO | [History](https://finance.yahoo.com/quote/VOO/history/) | `https://query1.finance.yahoo.com/v8/finance/chart/VOO` |
| QQQ | [History](https://finance.yahoo.com/quote/QQQ/history/) | `https://query1.finance.yahoo.com/v8/finance/chart/QQQ` |
| SOXX | [History](https://finance.yahoo.com/quote/SOXX/history/) | `https://query1.finance.yahoo.com/v8/finance/chart/SOXX` |
| SCHD | [History](https://finance.yahoo.com/quote/SCHD/history/) | `https://query1.finance.yahoo.com/v8/finance/chart/SCHD` |
| BIL | [History](https://finance.yahoo.com/quote/BIL/history/) | `https://query1.finance.yahoo.com/v8/finance/chart/BIL` |
| BND | [History](https://finance.yahoo.com/quote/BND/history/) | `https://query1.finance.yahoo.com/v8/finance/chart/BND` |

Query: `period1=1633046400`, `period2=1790812800`, `interval=1mo`, `events=div,splits`, `includeAdjustedClose=true`. These boundaries are October 1, 2021 inclusive and October 1, 2026 exclusive, in UTC.

The program received 60 required month keys per ticker, October 2021 through September 2026, and validated that every adjusted close was positive and finite. It normalized dates to calendar month end and wrote prices to six decimal places. Provider monthly prices include provider dividend/split adjustments. No missing values were filled and October 2026 was excluded as unfinished. See the exact request construction and transformations in [build_prices.py](https://github.com/edheeres05/Lab15WebAPP/blob/main/build_prices.py).

Original source documentation SHA-256: `4db0e28aa81cf8642a5ff756777cf844eb300cffec669e170bbc6e9e8285010a`

Sample estimates: 59 monthly returns (all) or 36 monthly returns (recent). Sample standard deviation uses `ddof=1`; the return estimate is arithmetic monthly mean × 12. Correlations use the same complete return rows. Last 36 requires 37 prices; calculation occurs before slicing returns.

Prices are a retrieval-date snapshot, not a contemporaneous archive of information available at each historical decision date. These data do not establish point-in-time validity, forecast accuracy or net performance. Adjusted prices can be revised later.

The original repository includes a downloader; it is intentionally omitted from this reproduction bundle to preserve the existing snapshot. It overwrites `prices.csv`; preserve this snapshot and update the retrieval date, checksum and reported results if you rerun it. For reproducibility, the saved results and tests refer to the bundled October 22 snapshot.


## Package source

The app, engine, prices and requirements were copied from `edheeres05/Lab15WebAPP` on November 17, 2026. No current market data were fetched for this package. The retrieval date above is the original repository's recorded provenance, not a new independent data-source verification.

- `app.py` source blob SHA: `e03d78d28bbee29bbaea09d825e9098efa0b5566`.
- `portfolio.py` source blob SHA: `26345a2a37fd159461d6f21203f9779cb5b7aabb`.
- `prices.csv` source blob SHA: `4c668c23fa9197221b867d38d6cd87acac375eb3`.
- `requirements.txt` source blob SHA: `09e9f50ddab2eb9bd160f6606b5c5df60908b454`.

Packaged CSV SHA-256: `cfbb60a1ab9c7bfc4355b9edcebfbe9ff64117a916021667b3e4067d7b1c2e34`. The packaged text has a different byte checksum from the original documented checksum; the original checksum is retained only as source documentation. The reproduced weights and numerical results match the existing GitHub baseline within 1e-12.
