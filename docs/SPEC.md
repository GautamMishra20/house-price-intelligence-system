# Bengaluru House Price Intelligence System — Project Spec

## 1. Project Title & One-Line Pitch

**Title:** Bengaluru House Price Intelligence System

**Pitch:** An end-to-end MLOps system that doesn't just predict house prices in Bengaluru — it tells you if a listing is fairly priced, why, and what comparable homes cost, with the full pipeline production-tracked via ZenML, MLflow, and CI/CD.

## 2. Problem Statement

Most house price predictors output a single number with no context. Buyers and sellers can't act on a bare price estimate — they need to know how confident the estimate is, why the model arrived at it, and whether a listing is a good deal relative to comparable properties. This project closes that gap by turning a point prediction into a full analytical report.

## 3. Scope — Locked Core (must ship in 2 weeks)

- Bengaluru house price dataset (Kaggle), full data validation + feature engineering pipeline
- ZenML-orchestrated pipeline: ingestion → validation → transformation → training → evaluation → registry
- Multi-algorithm comparison (e.g. Linear Regression, Random Forest, XGBoost, LightGBM) with all runs tracked under one MLflow experiment, best model auto-selected by metric
- MLflow experiment tracking + model registry
- DVC for data versioning
- Predicted price + confidence interval (range, not point estimate)
- Similar properties comparison (nearest-neighbor lookup on engineered features)
- Overpriced/underpriced detection vs. comparables
- SHAP-based explainability per prediction (per-feature contribution to that specific prediction)
- FastAPI serving layer + Streamlit dashboard
- Dockerized services + GitHub Actions CI (tests + lint, build image)

## 4. Stretch Scope (only if core finishes early)

- Live scraping of new Bengaluru listings from a property site (subject to site ToS/robots.txt)
- Scheduled retraining trigger when enough new data accumulates
- Basic monitoring dashboard for data/prediction drift

**Rationale for splitting this out:** real-time data infrastructure is independent of the ML system's quality — safer to add once the core is provably working than to risk both being half-done in a 2-week window.

## 5. Out of Scope (explicit, to prevent scope creep)

- Multi-city support (Bengaluru only for v1)
- User authentication / multi-tenant system
- Mobile app or production-grade frontend (Streamlit is sufficient for v1)
- A/B testing infrastructure for model versions

## 6. Success Criteria

- Pipeline runs end-to-end via a single ZenML command with no manual intervention
- Multiple algorithms trained and logged as separate MLflow runs under one experiment; best model selected by evaluation metric and promoted to the registry (selection is automatic, not manually picked)
- Model evaluation metric target: R² ≥ 0.80, with RMSE within an acceptable percentage of average price (exact thresholds finalized after EDA, once price distribution is known)
- API returns a full prediction report — price + confidence range + comparables + over/underpriced flag + SHAP-based reasons — in under 2 seconds
- CI pipeline passes on every push; Docker image builds cleanly
- README + short demo video ready for portfolio/resume use

## 7. Tech Stack

| Layer               | Tool                                                                            |
| ------------------- | ------------------------------------------------------------------------------- |
| Orchestration       | ZenML                                                                           |
| Experiment tracking | MLflow                                                                          |
| Data versioning     | DVC                                                                             |
| Modeling            | scikit-learn (Linear Regression, Ridge/Lasso, Random Forest), XGBoost, LightGBM |
| Explainability      | SHAP                                                                            |
| Serving             | FastAPI                                                                         |
| Dashboard           | Streamlit                                                                       |
| Containerization    | Docker, docker-compose                                                          |
| CI/CD               | GitHub Actions                                                                  |
| Dataset             | Kaggle — Bengaluru House Price dataset                                          |

## 8. Timeline (2 weeks)

- **Days 1–3:** Project skeleton, DVC setup, data ingestion + validation
- **Days 4–6:** Feature engineering, ZenML + MLflow training pipeline across multiple algorithms, evaluation + auto-selection of best model
- **Days 7–10:** Differentiation layer — confidence ranges, comparables, overpriced detection, SHAP explainability
- **Days 11–12:** FastAPI + Streamlit, Docker, GitHub Actions CI/CD
- **Days 13–14:** Polish — README, demo video/GIF, buffer for whatever breaks

**Fallback rule:** if days 13–14 buffer gets eaten by an earlier delay, cut scope from the bottom of Section 3 (Locked Core), not from documentation/demo — an unfinished feature is recoverable in a v1.1; a project with no README or demo is not portfolio-ready regardless of what's under the hood.

## 9. Notes

- All example metric values above (R² target, RMSE threshold) are placeholders to be finalized once EDA is complete — they are not yet derived from real model results.
- This document is the source of truth for scope decisions during the build. If a mid-build idea isn't in Section 3, it goes into Section 4 or gets logged separately for a v2 — it does not get added to the 2-week sprint.
