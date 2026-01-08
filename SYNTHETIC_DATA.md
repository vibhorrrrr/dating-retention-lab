# Why Synthetic Data Is Used

This project intentionally uses **synthetic data** instead of real dating app data.  
This choice is methodological, not convenient.

Below is a simple explanation of why this is the *correct* decision for this type of analysis.

---

## The problem with real-world dating data

Using real dating app data introduces several unsolvable issues:

### 1. Data access and ethics
Real dating data is private, sensitive, and legally restricted.  
Even anonymized datasets suffer from consent, bias, and leakage risks.

Using synthetic data avoids unethical assumptions entirely.

---

### 2. Confounding everywhere
In real systems, outcomes are influenced by:
- marketing campaigns
- seasonal effects
- app UI changes
- user self-selection
- hidden ranking rules

These confounders make causal conclusions unreliable.

You observe correlations, not mechanisms.

---

### 3. No counterfactuals
With real data, you cannot answer:
> What would have happened if the same users were exposed to a different algorithm?

Synthetic environments allow **counterfactual experimentation**, which real platforms cannot safely run.

---

## What synthetic data enables

Synthetic data allows us to isolate **causal structure**, not chase noisy realism.

Specifically, it enables:

### Controlled user behavior
Each user has explicit parameters:
- baseline churn
- commitment
- selectiveness
- attractiveness

These traits are fixed and observable.

---

### Algorithm-level interventions
We can change **only the matching logic** while holding everything else constant.

This isolates the effect of:
- love optimization
- retention optimization

No hidden policy changes. No unobserved shifts.

---

### Repeatability
Every experiment can be rerun with the same seed.
Results are reproducible.
Sensitivity can be stress-tested.

This is impossible with production data streams.

---

## Are the insights invalid because the data is synthetic?

No.  
This is a misunderstanding of what the project claims.

### What this project does NOT claim
- It does not predict outcomes for any specific dating app
- It does not estimate real-world effect sizes
- It does not model real user psychology in full detail

---

### What this project DOES claim
- The trade-off between retention and relationship success is **structural**
- Optimizing for one objective degrades the other under broad assumptions
- The result holds across wide parameter ranges

This is a **mechanism-level insight**, not a forecasting exercise.

---

## Analogy

Synthetic data here plays the same role as:

- frictionless planes in physics
- agent-based models in economics
- simulations in systems engineering

They are not “fake”.
They are **controlled abstractions**.

---

## Why this matters

Most platform discussions argue at the level of intent or ethics.

This project shows that:
- even well-designed systems face objective trade-offs
- incentives shape outcomes more than stated goals
- retention and user happiness are not aligned by default

Synthetic data makes this visible.

---

## Bottom line

> Synthetic data is not a weakness here.  
> It is the only way to make the causal question answerable.

If you want realism, collect logs.  
If you want understanding, build simulations.

This project chooses understanding.
