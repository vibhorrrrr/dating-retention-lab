import pandas as pd
from pathlib import Path

from src.generate_users import generate_users
from src.simulator import simulate

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
OUT_FILE = DATA_DIR / "simulation_results.csv"

users = generate_users(n_users=2000)
df = simulate(users, n_weeks=12, seed=1)

df.to_csv(OUT_FILE, index=False)

print("Simulation complete")
print("Saved to:", OUT_FILE)
print()

print("Relationship rate by algorithm")
print(df.groupby("algo")["relationship"].mean())
print()

final_week = df["week"].max()
retained = (
    df[df.week == final_week]
    .groupby("algo")["user_id"]
    .nunique()
)

print("Retained users at final week")
print(retained)
