ChatGPT assisted with code development, packaging, verification and writing. Ethan supplied the prediction ideas, portfolio choice and partner report and is responsible for the analysis and decision.

Education, not investment advice.

# FIN 439 — Lab 20: Project 2 Readiness
Ethan Heeres

**Decision: Pilot for educational testing only.** The app reproduces the six-fund baseline, and the partner reported a clean cold run. The changed-input test remains feasible but increases risk, so it does not support adoption for real investment use. Reject the pilot if an input change makes the selected return/reserve screens infeasible or if the saved calculations cannot be reproduced.

- [Lab 20 write-up](Lab20_EthanHeeres.md)
- [Before output](before.md)
- [After output](after.md)
- [Prediction committed before the changed-input run](https://github.com/edheeres05/Lab20/commit/a708628f404a89549e0dd33239ec06c834e876ec)

## Download and run

On GitHub, select **Code → Download ZIP**, then extract it. Open the extracted folder in VS Code. Open the folder that directly contains `app.py` and `requirements.txt`; do not stop at an outer folder that contains only another folder.

In VS Code, select **Terminal → New Terminal** and install the dependencies:

```powershell
py -m pip install -r requirements.txt
```

Start the app:

```powershell
py -m streamlit run app.py
```

If your installation uses `python`, replace `py` with `python`. Keep the terminal open. Open the Local URL printed by Streamlit if the browser does not open automatically.

### Select the six-fund baseline after every restart

The app starts with the Meridian training example. For this lab:

1. Check **Use included six-fund prices.csv**. No upload is necessary.
2. Click **Use proposed project settings: 6% / 5%**.
3. Keep **Use only the last 36 monthly returns** off.
4. Keep only **BIL** reserve-eligible.
5. Leave the six return estimates unchanged.

The baseline is 0% VOO, 5% QQQ, 5% SOXX, 5% SCHD, 85% BIL and 0% BND: **6.08% estimated annual gross return and 3.33% volatility**.

### Reproduce the saved baseline with one command

After installing dependencies, run:

```powershell
py reproduce.py
```

This prints the baseline and saves [outputs/baseline.md](outputs/baseline.md) and [outputs/baseline.json](outputs/baseline.json). The output is readable on GitHub without running Python.

### Repeat the recorded changed-input test

Starting from the six-fund baseline, set **SOXX expected return (%)** to **25.00** and press Enter while the cursor is in that box. Leave everything else unchanged.

The current-input mix becomes 5% VOO, 5% QQQ, 5% SOXX, 5% SCHD, 80% BIL and 0% BND: **6.10% estimated annual gross return and 4.04% volatility**. The reference mix on the right stays at the original result.

The button **Download this comparison as Markdown** creates `Lab15_scenario_snapshot.md`. It is a new browser download, not an existing project file. The two recorded downloads are preserved here as `before.md` and `after.md`. Their original Lab 15 export headings are retained.

## Scope

The selected universe is VOO, QQQ, SOXX, SCHD, BIL and BND. No ORCL substitution is used. The engine minimizes estimated volatility on a 5-percentage-point grid with nonnegative weights summing to 100%, a 6% gross-return minimum and a 5% BIL minimum.

The estimates use the saved monthly prices and are historical arithmetic estimates, not forecasts. Costs and taxes are excluded. Full Project 2 net-return, timing and policy compliance is not established by this lab. See the write-up for the readiness assessment and [DATA_SOURCES.md](DATA_SOURCES.md) for provenance.

## Files

| File | Purpose |
|---|---|
| `Lab20_EthanHeeres.md` | Cold-run note, prediction commit, actual results and decision |
| `before.md`, `after.md` | Student-downloaded before/after evidence |
| `app.py` | Interactive Streamlit app |
| `portfolio.py` | Calculation engine |
| `prices.csv` | Saved monthly prices |
| `requirements.txt` | Dependencies |
| `reproduce.py` | Baseline reproduction command |
| `outputs/baseline.md`, `outputs/baseline.json` | Readable and unrounded baseline |
| `DATA_SOURCES.md` | Data sources and limitations |
| `.gitignore` | Excludes generated Python caches from future Git commits |
