# Lab 20 — Project 2 Readiness
Ethan Heeres | FIN 439 | November 17, 2026

ChatGPT helped inspect the repositories, package the existing app, reproduce its baseline, and draft this record. Human-only activities are marked unresolved rather than claimed as completed.

Education, not investment advice.

**Status: readiness draft — six-fund version confirmed; partner evidence, AI-off prediction, remaining mandate requirements and personal reflection unresolved.**

## D — The question

Could a committee member who has never met me reach my decision from my repository, and does the decision survive one changed input?

**Not yet established.** The inspected `FIN439project2` main branch contained `Lab13_EthanHeeres.md`, `mandate.py`, and a Lab 14 ZIP, with no root README or integrated web app. The runnable app was in the separate `Lab15WebAPP` repository. A reader could reproduce that exercise, but the final Project 2 mandate and decision were not demonstrated by the inspected Project 2 files alone.

On November 17, 2026, I selected the six-fund version: VOO, QQQ, SOXX, SCHD, BIL and BND. All six funds are retained, with no ORCL substitution. This replaces the universe in my earlier ORCL-focused proposal. The selected app minimizes estimated volatility with a 6% gross-return screen and at least 5% BIL. The other risk and policy requirements still need to be reconciled and implemented before full Project 2 mandate compliance can be claimed.

## R — Readiness check

| Part | Verified evidence | Remaining item |
|---|---|---|
| Tool | Existing interactive Lab 15 app and engine included | Six-fund version confirmed; reconcile remaining policy requirements and implement all final mandate verdicts |
| Repository / README | This package provides installation, app-start and result-reproduction commands | Upload to the existing repository and obtain partner's independent cold run |
| Visible output | `outputs/baseline.md` and JSON reproduce the existing six-fund result | Final Project 2 output must use the confirmed mandate |
| Decision memo | No `docs/decision-memo.md` in the inspected Project 2 tree | Supply or create the final memo after mandate confirmation |
| Validation and AI use | Existing baseline reproduced; limitations disclosed | Full baseline comparisons, point-in-time integration, stress checks and Locked Changed-Input Record |
| Videos 1–3 and transcripts | No links found in the inspected Project 2 tree | Supply working video/transcript links and manifest |
| Week 12 must-fix list | Not supplied or found in the inspected Project 2 tree | Ethan to provide the actual list |
| Due date | Not checked in Brightspace | Read the Project 2 assignment header; do not substitute an assumed date |

### Existing baseline reproduced with AI assistance

Run `py reproduce.py` from this folder. Source: the existing six-fund monthly price snapshot, October 2021–September 2026, producing 59 monthly returns.

| Metric | Existing six-fund exercise |
|---|---:|
| Estimated annual gross return | 6.08% |
| Estimated annual volatility | 3.33% |
| Reserve-eligible weight | 85.00% |
| VOO / QQQ / SOXX / SCHD / BIL / BND weights | 0 / 5 / 5 / 5 / 85 / 0% |

Settings: at least 6% estimated gross annual return, at least 5% BIL, nonnegative weights summing to 100%, 5-percentage-point grid, minimum estimated volatility. This does not establish the net-return target, full mandate compliance, future performance or point-in-time validity.

## I — Partner's cold run

**Unresolved — no Lab 20 partner observation has been provided.** The AI-assisted reproduction above is not a partner cold run. Earlier partner discussions are not reused as today's evidence.

| Required observation | Partner's actual note |
|---|---|
| Partner name | UNRESOLVED |
| Repository link and commit tested | UNRESOLVED |
| Exact command(s) entered | UNRESOLVED |
| First failure and exact error, or an explicit clean run | UNRESOLVED |
| Elapsed time | UNRESOLVED |
| Result location and numbers reached | UNRESOLVED |

## V — Locked Changed-Input Record

**Unresolved — no new Lab 20 changed-input run has been performed.** Close AI and write this prediction yourself before running. The earlier Lab 15 sensitivities are not a new AI-off prediction.

### Before the run — write personally, then commit and push

I will lower SOXX’s expected annual return from 33.89% to 25%. I expect less allocation to SOXX, lower portfolio return, and lower volatility. My decision will remain Pilot because I expect a more conservative allocation with less exposure to the highly volatile semiconductor sector.

### After the prediction commit — run and record

- Actual after-output link: UNRESOLVED.
- Before/after decision numbers: UNRESOLVED.
- Does the decision change? UNRESOLVED.
- Why the actual result matches or differs from the prediction, or why nothing changes: UNRESOLVED.

Preserve both outputs and the original prediction commit. Do not rewrite a prediction after seeing the result.

## Explain the code

**Unresolved — complete the six-minute discussion with AI closed.**

- Code block explained: UNRESOLVED.
- Partner's actual question: UNRESOLVED.
- My answer from the code: UNRESOLVED.
- Line I could not explain, if any: UNRESOLVED.

## E — Fix one thing

**AI-assisted preparation completed:** packaged the existing application and inputs with a README, a result-reproduction command, and readable baseline output. This addresses the observed packaging/entry-point gap, but it is not claimed as the first failure encountered by a partner.

- Partner's first failure: UNRESOLVED.
- Fix made in response, or confirmed clean run with no fix needed: UNRESOLVED.
- Fix commit URL: UNRESOLVED — nothing pushed.
- Partner's rerun result: UNRESOLVED.

## Decision line

**Draft for Ethan to review, based on the earlier Lab 15 pilot position:** Pilot the six-fund model for educational evaluation only; reject the process for investment use unless the final mandate is reconciled and the required cost, risk, timing and reproducibility checks are completed.

The six-fund version is confirmed. This proposed readiness decision does not claim that the complete mandate has been finalized or an investment allocation approved. The response to the new changed input is still unresolved.

## Reflect

Complete from the actual partner discussion:

1. What the cold run found that I could not see: UNRESOLVED.
2. What I will not touch before the deadline: UNRESOLVED.

## Checkout

After uploading to the **existing** repository, submit GitHub links for this Markdown file and the code/data files needed to run the app. The README and visible output should also be reachable there. The ZIP itself is a download bundle; it does not replace the requested GitHub file links.

Quiz completion, partner activities, commits, videos and Brightspace submission have not been claimed.

Assignment: [Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md). The assignment permits truthful unresolved items; it does not grade or approve Project 2.
