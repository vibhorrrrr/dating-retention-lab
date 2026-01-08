import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "simulation_results.csv"
FIG_PATH = Path(__file__).resolve().parents[1] / "figures" / "love_vs_retention.png"

# Load data
df = pd.read_csv(DATA_PATH)

# Aggregate stats
relationship_rate = df.groupby("algo")["relationship"].mean()
final_week = df["week"].max()
retained = (
    df[df.week == final_week]
    .groupby("algo")["user_id"]
    .nunique()
)

retention_curve = (
    df.groupby(["algo", "week"])["user_id"]
    .nunique()
    .reset_index()
)

# Colors
LOVE_COLOR = "#e53935"        # volatile red
RETENTION_COLOR = "#1e88e5"   # stable blue

plt.rcParams.update({
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.labelsize": 11
})

fig = plt.figure(figsize=(14, 9))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1])

# --- 1. Relationship formation ---
ax1 = fig.add_subplot(gs[0, 0])
bars = ax1.bar(
    relationship_rate.index,
    relationship_rate.values,
    color=[LOVE_COLOR, RETENTION_COLOR],
    alpha=0.9
)

ax1.set_title("Relationship Formation Rate")
ax1.set_ylabel("Probability")
ax1.set_ylim(0, relationship_rate.max() * 1.3)

for bar in bars:
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height()*100:.1f}%",
        ha="center",
        va="bottom",
        fontweight="bold"
    )

ax1.spines[['top', 'right']].set_visible(False)

# --- 2. Retention curves ---
ax2 = fig.add_subplot(gs[0, 1])

for algo, color in [("love", LOVE_COLOR), ("retention", RETENTION_COLOR)]:
    sub = retention_curve[retention_curve.algo == algo]
    ax2.plot(
        sub.week,
        sub.user_id,
        label=algo.capitalize(),
        linewidth=3,
        color=color
    )

ax2.set_title("User Retention Over Time")
ax2.set_xlabel("Week")
ax2.set_ylabel("Active Users")
ax2.legend(frameon=False)
ax2.grid(alpha=0.2)
ax2.spines[['top', 'right']].set_visible(False)

# --- 3. Final retained users ---
ax3 = fig.add_subplot(gs[1, 0])
bars = ax3.bar(
    retained.index,
    retained.values,
    color=[LOVE_COLOR, RETENTION_COLOR],
    alpha=0.9
)

ax3.set_title("Users Retained at Final Week")
ax3.set_ylabel("Users")

for bar in bars:
    ax3.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height())}",
        ha="center",
        va="bottom",
        fontweight="bold"
    )

ax3.spines[['top', 'right']].set_visible(False)

# --- 4. Insight box ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis("off")

insight = (
    "Key Insight\n\n"
    "Optimizing for love maximizes matches but accelerates churn.\n\n"
    "Optimizing for retention reduces short-term excitement but\n"
    "keeps significantly more users alive over time.\n\n"
    "Metrics define behavior.\n"
    "Behavior defines outcomes."
)

ax4.text(
    0,
    0.5,
    insight,
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor="#f5f5f5", alpha=0.95)
)

# --- Global title ---
fig.suptitle(
    "Love vs Retention Algorithms\nSame Users. Very Different Outcomes.",
    fontsize=18,
    fontweight="bold",
    y=0.98
)

plt.tight_layout()
plt.savefig(FIG_PATH, dpi=200)
plt.show()

print("Visualization saved to:", FIG_PATH)
