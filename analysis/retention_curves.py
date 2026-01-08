import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/simulation_results.csv")
FIG_PATH = Path("figures/retention_curves.png")

df = pd.read_csv(DATA_PATH)

# Retention proxy: users appearing in later weeks
retention = (
    df.groupby(["algo", "week"])["user_id"]
    .nunique()
    .reset_index()
)

plt.figure(figsize=(8, 5))

for algo in ["love", "retention"]:
    subset = retention[retention.algo == algo]
    plt.plot(
        subset.week,
        subset.user_id,
        label=f"{algo.capitalize()}-Optimized"
    )

plt.xlabel("Week")
plt.ylabel("Active Users")
plt.title("Retention Over Time by Optimization Strategy")
plt.legend()
plt.tight_layout()

FIG_PATH.parent.mkdir(exist_ok=True)
plt.savefig(FIG_PATH, dpi=200)
plt.show()
