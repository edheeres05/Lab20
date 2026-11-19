
Education, not investment advice.

# Lab 20 — Project 2 Readiness
Ethan Heeres | FIN 439 | Session 20

## D — Can a stranger reproduce the decision?

The six-fund app can be run from the repository instructions, and Gage Hodson reported reaching the same baseline without errors. The changed-input test still meets the app's return and reserve screens, but it increases estimated volatility instead of reducing it. The recommendation is a limited educational pilot, not adoption for real investment use.

The selected universe is VOO, QQQ, SOXX, SCHD, BIL and BND. This replaces the earlier ORCL-focused universe for this lab. The objective implemented here is to minimize estimated volatility on a 5-percentage-point allocation grid, subject to nonnegative weights totaling 100%, at least 6% estimated annual gross return and at least 5% BIL.

## I — Partner cold-run note

**Partner:** Gage Hodson.

Gage downloaded the repository files, opened them in VS Code and ran the README's installation and app-start commands in the terminal:

```powershell
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

| Required observation | Report |
|---|---|
| Repository | [edheeres05/Lab20](https://github.com/edheeres05/Lab20) |
| First failure | No errors reported |
| Elapsed time | Approximately 13.5 minutes to get the app running |
| Result location | Streamlit app in the browser |
| Result reached | Same six-fund baseline: 6.08% estimated annual gross return and 3.33% annual volatility |

This note records the partner experience reported by Ethan. The AI-assisted verification is separate from Gage's cold run.

## V — Changed input: prediction and result

### Prediction preserved before the changed-input run

[Prediction commit: a708628](https://github.com/edheeres05/Lab20/commit/a708628f404a89549e0dd33239ec06c834e876ec)

The prediction was committed on November 17, 2026, at 5:11:49 p.m. Eastern. Its original text is preserved:

> I will lower SOXX’s expected annual return from 33.89% to 25%. I expect less allocation to SOXX, lower portfolio return, and lower volatility. My decision will remain Pilot because I expect a more conservative allocation with less exposure to the highly volatile semiconductor sector.

The old displayed estimate was 33.89%; the exported unrounded assumption was 33.894245%. The new estimate is 25.000000% per year. Only SOXX's return estimate changed. The target stayed at 6%, the reserve minimum stayed at 5%, only BIL remained reserve-eligible, and all 59 monthly returns were used. Volatilities and correlations were unchanged.

**AI-use disclosure:** I supplied the prediction ideas before running the change. AI clarified the prompt and polished the wording before the commit. This is not represented as a completely AI-off prediction.

### Saved evidence

- [Before output](before.md)
- [After output](after.md)

| Holding | Before | After | Change |
|---|---:|---:|---:|
| VOO | 0% | 5% | +5 percentage points |
| QQQ | 5% | 5% | 0 |
| SOXX | 5% | 5% | 0 |
| SCHD | 5% | 5% | 0 |
| BIL | 85% | 80% | −5 percentage points |
| BND | 0% | 0% | 0 |

| Decision number | Before | After |
|---|---:|---:|
| Estimated annual gross return | 6.08% | 6.10% |
| Estimated annual volatility | 3.33% | 4.04% |
| Reserve-eligible weight | 85.00% | 80.00% |
| Meets the 6% gross-return screen | Yes | Yes |
| Meets the 5% BIL reserve screen | Yes | Yes |

The largest allocation change was 5 percentage points. Return increased by approximately 0.02 percentage points and volatility increased by approximately 0.71 percentage points, using the displayed rounded results.

### Why the result differed from the prediction

My prediction did not match the allocation or risk result. SOXX stayed at 5%, and the optimizer moved 5 percentage points from BIL to VOO. Lowering SOXX's return estimate did not lower its volatility assumption.

With the original weights held fixed, the lower SOXX estimate would reduce portfolio expected return to approximately 5.63%, below the unchanged 6% target. The optimizer therefore had to select a different feasible mix. It added VOO and reduced BIL to regain the target, which increased estimated volatility. The after result's slightly higher return reflects the newly selected mix on the 5-point grid; it does not mean lowering an asset's assumed return improved the original portfolio.

### Effect on the decision

The recommendation remains **Pilot for educational testing only**. The rationale is limited testing and further validation, not the predicted reduction in risk: this run actually increased risk. Remaining feasible under the selected screens supports continuing the exercise, but does not establish that the process is ready for real-money adoption.

## E — Fix one thing

Gage reported a clean cold run. **No fix was needed**, so there is no repair commit or repair rerun to report. The final README clarifies how to select the six-fund preset after a restart; this documentation clarification is not presented as a repair of a failure Gage encountered.

## Decision line

**Pilot the six-fund process for educational testing only; reverse to reject if a changed input makes the selected return/reserve screens infeasible or the saved calculations cannot be reproduced.**

## R — Project 2 readiness assessment

| Manifest part | Evidence and current status |
|---|---|
| Tool | Runnable Streamlit app with editable return assumptions and portfolio results. The current app enforces the limited exercise screens, not the complete Project 2 mandate. |
| Repository | README supplies installation, app-start and single-command baseline reproduction instructions. Gage reported a clean cold run. |
| Visible output | Before and after Markdown files and baseline output are readable on GitHub. |
| Decision memo | The decision is recorded in this Lab 20 write-up. A separate final Project 2 decision memo is not included. |
| Validation and AI use | Baseline reproduction, one changed-return-estimate test, prediction commit and AI disclosure are documented. Full Project 2 baseline verdicts, cost/window/constraint stress coverage and integrated point-in-time evidence are not established by this package. |
| Videos and transcripts | Project 2 video and transcript links are not included in this Lab 20 package. |

The data are a saved adjusted-price snapshot, not a point-in-time archive. Return estimates are arithmetic historical means, not forecasts. Trading costs and taxes are excluded. The model's grid minimum is not an exact continuous optimum. The complete Project 2 mandate is not validated by the two exercise screens.

This is the Lab 20 readiness record, not a claim that the entire Project 2 submission is complete. The assignment permits truthful unresolved readiness items.

## Checkout links

- [Repository and README](https://github.com/edheeres05/Lab20)
- [Lab 20 Markdown](https://github.com/edheeres05/Lab20/blob/main/Lab20_EthanHeeres.md)
- [Application](https://github.com/edheeres05/Lab20/blob/main/app.py)
- [Calculation engine](https://github.com/edheeres05/Lab20/blob/main/portfolio.py)
- [Before evidence](https://github.com/edheeres05/Lab20/blob/main/before.md)
- [After evidence](https://github.com/edheeres05/Lab20/blob/main/after.md)

Assignment: [Lab 20 — Project 2 Readiness](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md).
