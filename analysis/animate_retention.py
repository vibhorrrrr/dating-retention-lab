import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "simulation_results.csv"
FIG_PATH = Path(__file__).resolve().parents[1] / "figures" / "retention_animation.gif"

# Load data
df = pd.read_csv(DATA_PATH)

# Prepare retention curves
retention = (
    df.groupby(["algo", "week"])["user_id"]
    .nunique()
    .reset_index()
)

weeks = sorted(retention.week.unique())

love = retention[retention.algo == "love"]
ret = retention[retention.algo == "retention"]

# Colors
LOVE_COLOR = "#e53935"
RET_COLOR = "#1e88e5"

# Figure setup
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_xlim(min(weeks), max(weeks))
ax.set_ylim(
    0,
    max(ret.user_id.max(), love.user_id.max()) * 1.1
)

ax.set_title(
    "User Retention Over Time\nLove vs Retention Algorithms",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Week")
ax.set_ylabel("Active Users")

ax.grid(alpha=0.2)
ax.spines[['top', 'right']].set_visible(False)

# Initialize lines
love_line, = ax.plot([], [], color=LOVE_COLOR, linewidth=3, label="Love Optimized")
ret_line, = ax.plot([], [], color=RET_COLOR, linewidth=3, label="Retention Optimized")

ax.legend(frameon=False)

# Animation function
def update(frame):
    current_weeks = weeks[:frame + 1]

    love_y = love[love.week.isin(current_weeks)].user_id.values
    ret_y = ret[ret.week.isin(current_weeks)].user_id.values

    love_line.set_data(current_weeks, love_y)
    ret_line.set_data(current_weeks, ret_y)

    ax.set_title(
        f"User Retention Over Time\nWeek {current_weeks[-1]}",
        fontsize=16,
        fontweight="bold"
    )

    return love_line, ret_line

# Animate
anim = FuncAnimation(
    fig,
    update,
    frames=len(weeks),
    interval=600,
    blit=True
)

# Save animation
anim.save(FIG_PATH, writer="pillow", fps=2)


plt.show()

print("Retention animation saved to:", FIG_PATH)
