import pandas as pd
from pathlib import Path
from src.generate_users import generate_users
from src.simulator import simulate

OUT_PATH = Path(__file__).resolve().parents[1] / "data" / "sensitivity_results.csv"

results = []

# Sensitivity dimensions
churn_multipliers = [0.5, 1.0, 1.5]
match_strengths = [0.5, 1.0, 1.5]

for churn_mult in churn_multipliers:
    for match_strength in match_strengths:

        # 1. Generate users
        users = generate_users(n_users=2000, seed=42)

        # 2. Scale churn externally
        users = users.copy()
        users["churn_base"] *= churn_mult

        # 3. Run both algorithms
        love = simulate(
            users,
            algo="love",
            n_weeks=12,
            match_strength=match_strength,
            seed=1
        )

        retention = simulate(
            users,
            algo="retention",
            n_weeks=12,
            match_strength=match_strength,
            seed=1
        )

        # 4. Collect metrics
        for label, df in [("love", love), ("retention", retention)]:
            final_week = df.week.max()
            retained = df[df.week == final_week]["user_id"].nunique()
            relationship_rate = df["relationship"].mean()

            results.append({
                "algo": label,
                "churn_multiplier": churn_mult,
                "match_strength": match_strength,
                "retained_users": retained,
                "relationship_rate": relationship_rate
            })

pd.DataFrame(results).to_csv(OUT_PATH, index=False)

print("Sensitivity analysis complete")
print("Saved to:", OUT_PATH)
