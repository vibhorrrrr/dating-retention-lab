# FAQ

This FAQ addresses the most common objections raised when people see this project.
If a question sounds aggressive, that is intentional. These are real critiques.

---

## “This uses synthetic data. Aren’t the results meaningless?”

No.

Synthetic data is used because the goal is **causal understanding**, not prediction.

Real-world dating data is:
- proprietary
- confounded
- non-reproducible
- ethically constrained

Using it would prevent counterfactual reasoning entirely.

This project studies **mechanisms**, not metrics from a specific app.

---

## “But real users don’t behave like this.”

Correct. And irrelevant.

No simulation perfectly captures reality. That is not the bar.

The question is:
> Does the result persist across reasonable behavioral assumptions?

This project answers that using:
- sensitivity analysis
- parameter sweeps
- Pareto frontiers
- counterfactual policy switches

If the result survives variation, it is structural.

---

## “You tuned the simulation to get the result you wanted.”

No.

Parameters were varied across wide ranges:
- churn rates
- selectiveness
- commitment distributions
- match thresholds

The trade-off between retention and relationship success persists.

If the result vanished under small perturbations, it would be discarded.

---

## “Why not validate this with real data?”

Because real platforms cannot run the required counterfactuals.

You cannot safely test:
- the same users
- under two different algorithms
- at the same time
- without feedback contamination

Simulation is the only environment where this comparison is valid.

---

## “This is just a toy model.”

Every model is a toy. The question is whether it is useful.

This model is useful because it:
- isolates incentives
- exposes second-order effects
- makes trade-offs explicit
- produces falsifiable claims

Complexity without control would make it worse, not better.

---

## “The effect sizes are unrealistic.”

Correct. And explicitly acknowledged.

Effect sizes here are **not estimates**.
They are **demonstrations of directionality and trade-off**.

No claim is made that real apps will see identical magnitudes.

---

## “So what is the real contribution then?”

The contribution is showing that:

- optimizing for love
- optimizing for retention

are **not the same problem** and cannot be solved by the same objective.

This is not an opinion.
It is a consequence of incentives under churn dynamics.

---

## “Isn’t this anti-dating-app or anti-growth?”

No.

It is anti-hand-waving.

The project does not say platforms are malicious.
It says that incentives shape outcomes, even with good intent.

That is a systems result, not a moral one.

---

## “Who is this project for?”

- product scientists
- growth teams
- ML engineers
- researchers interested in causal inference
- anyone building engagement-driven systems

It is not for people looking for vanity metrics.

---

## “What would falsify this result?”

Any of the following would invalidate the claim:
- retention optimization increases long-term relationship formation
- the trade-off disappears across parameter sweeps
- counterfactual switching shows no divergence

None of these occurred in the experiments.

---

## Final note

If your critique is:
> “This doesn’t perfectly represent reality”

You are correct.

If your critique is:
> “This makes a causal question answerable that real data cannot”

Then you understand the project.

This work chooses clarity over comfort.
