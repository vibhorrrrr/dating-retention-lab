import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.generate_users import generate_users
from src.simulator import simulate

ROOT = Path(__file__).resolve().parents[1]
FIG_PATH = ROOT / "figures" / "pareto_frontier.png"
FIG_PATH.parent.mkdir(exist_ok=True)

match_strengths = np.linspace(0.5, 2.0, 12)
algos = ["love", "retention"]

records = []

for algo in algos:
    for strength in match_strengths:
        users = generate_users(n_users=2000, seed=42)

        df = simulate(
            users,
            algo=algo,
            n_weeks=12,
            match_strength=strength,
            seed=1
        )

        final_week = df.week.max()

        retained = (
            df[df.week == final_week]
            .groupby("algo")["user_id"]
            .nunique()
            .iloc[0]
        )

        retention_rate = retained / users.user_id.nunique()
        relationship_rate = df.groupby("algo")["relationship"].mean().iloc[0]

        records.append({
            "algo": algo,
            "match_strength": strength,
            "retention": retention_rate,
            "relationships": relationship_rate
        })

res = pd.DataFrame(records)

# Plot
plt.figure(figsize=(8, 6))

for algo, grp in res.groupby("algo"):
    plt.plot(
        grp.retention,
        grp.relationships,
        marker="o",
        label=f"{algo} optimized"
    )

plt.xlabel("Final Retention Rate")
plt.ylabel("Relationship Formation Rate")
plt.title("Pareto Frontier: Retention vs Relationships")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_PATH, dpi=200)
plt.show()

print("Pareto frontier saved to:", FIG_PATH)
