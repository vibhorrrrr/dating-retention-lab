# Dating Retention Lab  
### When matchmaking algorithms optimize for growth instead of love

---

## Overview

Dating platforms publicly claim to optimize for meaningful relationships.  
In reality, their survival depends on retention.

This project simulates a dating app environment to study a fundamental question:

**What happens when matching algorithms optimize for retention instead of relationship success?**

Using controlled simulations, we compare two strategies:

- **Love-optimized matching**: maximizes compatibility and relationship formation  
- **Retention-optimized matching**: minimizes churn and keeps users active longer

The result is a measurable trade-off between short-term satisfaction and long-term platform growth.

---

## Why this matters

Most discussions around dating apps focus on user experience.  
This project reframes the problem as a **product and systems design question**.

Retention, not love, is the dominant optimization target in consumer platforms.

Understanding this trade-off explains:
- why many users stay active but dissatisfied
- why relationship success can decrease while engagement metrics improve
- how algorithmic incentives shape user outcomes

---

## Methodology

The system is fully simulated to allow causal control and repeatability.

### User generation
Each user is modeled with latent traits:
- attractiveness
- selectiveness
- commitment
- baseline churn probability

### Matching algorithms
Two scoring functions are implemented:

1. **Love-optimized**
   - prioritizes similarity and compatibility
   - increases probability of stable relationships
   - increases churn once relationships form

2. **Retention-optimized**
   - prioritizes novelty and uncertainty
   - suppresses relationship formation
   - minimizes churn and maximizes weekly activity

### Simulation
- Users interact weekly
- Matches influence relationship formation
- Relationships influence churn
- Users exit permanently when churned

All experiments run on identical user populations.

---

## Key experiments

### 1. Relationship formation comparison
Measures how often each algorithm leads to relationships.

**Result**  
Love optimization produces significantly higher relationship rates.  
Retention optimization suppresses relationships almost entirely.

---

### 2. Retention curves
Tracks active users over time.

**Result**  
Retention optimization keeps substantially more users active at later weeks, despite fewer successful matches.

---

### 3. Sensitivity analysis
Tests robustness across churn rates and behavioral parameters.

**Result**  
The trade-off persists across wide parameter ranges.  
The outcome is structural, not an artifact of tuning.

---

### 4. Pareto frontier
Visualizes the trade-off between retention and relationships.

**Result**  
No single policy dominates. Improving one objective necessarily worsens the other.

---

## Visual outputs

Generated figures include:
- Relationship rate comparison
- Retention curves over time
- Pareto frontier of outcomes
- Sensitivity heatmaps
- Animated retention dynamics

All figures are saved under `figures/`.

---

## Folder structure

```text
dating-retention-lab/
├── analysis/
│   ├── run_experiment.py
│   ├── retention_curves.py
│   ├── animate_retention.py
│   ├── pareto_frontier.py
│   ├── sensitivity_analysis.py
│   ├── sensitivity_heatmap.py
│   └── visualize_results.py
├── src/
│   ├── generate_users.py
│   ├── matching.py
│   └── simulator.py
├── data/
│   ├── simulation_results.csv
│   └── sensitivity_results.csv
├── figures/
│   └── generated plots and animations
└── README.md
````

---

## How to run

Run the core experiment:

```bash
python3 -m analysis.run_experiment
```

Generate visualizations:

```bash
python3 -m analysis.visualize_results
python3 -m analysis.animate_retention
```

Run sensitivity analysis:

```bash
python3 -m analysis.sensitivity_analysis
python3 -m analysis.sensitivity_heatmap
```

---

## Why synthetic data is used

Real dating data is inaccessible, biased, and ethically constrained.

Synthetic data allows:

* full control over causal mechanisms
* repeatable experiments
* stress testing across assumptions

The goal is **mechanism discovery**, not prediction of any specific platform.

The full reasoning can be viewed by clicking the below link or directly accessing the `/SYNTHETIC_DATA.md` file.

-> **[View reasoning](./SYNTHETIC_DATA.md)**

---

## Frequently Asked Question

The FAQs can be viewed by clicking the below link or directly accessing the `/FAQ.md` file.

-> **[View QnA](./FAQ.md)**

---

## Core insight

> Optimizing for love and optimizing for retention are not the same problem.
> Modern platforms choose one, then market the other.

---

## Disclaimer

This project is an analytical simulation.
It does not represent or target any real dating platform.

---

## Author

Built by **Vibhor Joshi**
Data science, causal inference, and product systems thinking

If this made you uncomfortable, it worked.
