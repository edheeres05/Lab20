ChatGPT assisted with assembling the existing code, checking reproduction, and drafting the readiness record. Ethan must review the analysis and own the final decision.

Education, not investment advice.

# Lab 20 — Ethan Heeres

This is a runnable readiness package based on the existing [Lab 15 app](https://github.com/edheeres05/Lab15WebAPP). **The Lab 20 record is a draft with explicit unresolved items.** It is not a completed Project 2 submission.

## Run on Windows

Extract this ZIP. Open the extracted `Lab20_EthanHeeres` folder in VS Code, then open Terminal → New Terminal. The terminal must show the folder containing `app.py`.

Install once:

```powershell
py -m pip install -r requirements.txt
```

Reproduce the saved six-fund result with one command:

```powershell
py reproduce.py
```

Read [the visible result](outputs/baseline.md) without running anything. The command writes that file and `outputs/baseline.json`.

Start the interactive app:

```powershell
py -m streamlit run app.py
```

If your system uses `python`, replace `py` with `python`. Python 3.10+ is recommended. Keep the terminal open while using the app.

The app initially shows the Meridian training case. To reproduce the six-fund result:

1. Check **Use included six-fund prices.csv**.
2. Click **Use proposed project settings: 6% / 5%**.
3. Leave **Use only the last 36 monthly returns** off.
4. Keep only BIL reserve-eligible and leave the return estimates unchanged.

Expected allocation in VOO / QQQ / SOXX / SCHD / BIL / BND: **0 / 5 / 5 / 5 / 85 / 0%**. Expected gross annual return **6.08%**, volatility **3.33%**, reserve **85%**.

These are historical estimates before costs. Passing this exercise's screens does not establish compliance with the full Project 2 mandate.

## Lab 20 workflow

- Use [Lab20_EthanHeeres.md](Lab20_EthanHeeres.md) for the individual checkout.
- Have your partner follow this README from your existing GitHub repository in their own folder. They must supply their actual command, first failure, elapsed time and result location.
- Close AI before writing your changed-input prediction in the lab record. Commit and push it to the existing repository **before** changing the input and running it.
- Save the app's current Markdown comparison as your before output. After the prediction commit, change only the chosen input and save another comparison under a different filename.
- Add the prediction commit URL, before/after output links, actual result, partner rerun and your own reflection.
- Submit the GitHub links requested in Brightspace. This package has not been pushed or submitted.

## Confirmed six-fund version

On November 17, 2026, Ethan selected the six-fund version: VOO, QQQ, SOXX, SCHD, BIL and BND. All six funds are retained; ORCL is not added. This selection supersedes the universe in the earlier [Lab 13 proposal](https://github.com/edheeres05/FIN439project2/blob/main/Lab13_EthanHeeres.md). The selected app minimizes estimated volatility subject to a 6% gross-return screen and at least 5% BIL. The remaining Project 2 policy requirements still need to be reconciled and implemented; choosing the universe does not establish full mandate compliance.

The complete Project 2 still requires a consistent mandate, two app baselines and their verdicts, point-in-time signal/data card, cost and other stress checks, decision memo, validation/AI-use record, videos/transcripts and manifest. See the readiness table in the lab record.

## Files

| File | Purpose |
|---|---|
| `Lab20_EthanHeeres.md` | Individual readiness draft; human evidence remains unresolved |
| `app.py` | Existing interactive app |
| `portfolio.py` | Existing calculation engine |
| `prices.csv` | Existing saved monthly price snapshot |
| `requirements.txt` | App dependencies |
| `reproduce.py` | Reproduce the existing six-fund result |
| `outputs/baseline.md` | Readable output for GitHub |
| `outputs/baseline.json` | Unrounded reproduction output |
| `DATA_SOURCES.md` | Existing data provenance and source file identifiers |

## Verification of this package

AI-assisted checks on November 17, 2026 reproduced the existing saved baseline within 1e-12 and exercised the app startup and six-fund preset using Streamlit AppTest. Checked with Python 3.12.14, Streamlit 1.67.0, pandas 2.2.3 and NumPy 2.3.5. These checks do not replace the partner cold run.
