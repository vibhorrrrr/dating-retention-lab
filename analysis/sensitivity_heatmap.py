import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.generate_users import generate_users
from src.simulator import simulate

# Paths
ROOT = Path(__file__).resolve().parents[1]
FIG_PATH = ROOT / "figures" / "sensitivity_heatmap.png"
FIG_PATH.parent.mkdir(exist_ok=True)

# Experiment grid
match_strengths = np.linspace(0.5, 2.0, 10)
algos = ["love", "retention"]

results = []

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

        final_week = df["week"].max()
        retained = (
            df[df.week == final_week]
            .groupby("algo")["user_id"]
            .nunique()
            .iloc[0]
        )

        retention_rate = retained / users["user_id"].nunique()

        results.append({
            "algo": algo,
            "match_strength": strength,
            "retention_rate": retention_rate
        })

res = pd.DataFrame(results)

# Pivot for heatmap
pivot = res.pivot(
    index="algo",
    columns="match_strength",
    values="retention_rate"
)

# Plot
plt.figure(figsize=(10, 4))
plt.imshow(pivot, aspect="auto", cmap="viridis")

plt.colorbar(label="Final Retention Rate")
plt.xticks(
    ticks=range(len(match_strengths)),
    labels=[f"{x:.1f}" for x in match_strengths]
)
plt.yticks(
    ticks=range(len(pivot.index)),
    labels=pivot.index
)

plt.xlabel("Match Strength")
plt.ylabel("Algorithm")
plt.title("Sensitivity Analysis: Retention vs Match Strength")

plt.tight_layout()
plt.savefig(FIG_PATH, dpi=200)
plt.show()

print("Sensitivity heatmap saved to:", FIG_PATH)
