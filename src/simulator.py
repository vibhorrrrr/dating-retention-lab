import numpy as np
import pandas as pd
from .matching import love_optimized_score, retention_optimized_score

def simulate(
    users,
    algo="love",
    n_weeks=12,
    seed=0,
    start_week=0,
    initial_state=None
):
    rng = np.random.default_rng(seed)

    if initial_state is None:
        alive = users.copy()
    else:
        # Resume from previous simulation
        alive = (
            initial_state
            .sort_values("week")
            .groupby("user_id")
            .tail(1)
            .query("alive == True")
            .drop(columns=["week", "algo", "relationship", "churn", "alive"])
            .copy()
        )

    records = []

    for week in range(start_week, start_week + n_weeks):

        if algo == "love":
            alive["match_quality"] = love_optimized_score(alive, rng)
        else:
            alive["match_quality"] = retention_optimized_score(alive, rng)

        alive["relationship"] = alive.match_quality > 0.7
        alive["churn_prob"] = alive.churn_base * (1 - alive.commitment)

        alive["churn"] = rng.random(len(alive)) < alive.churn_prob
        alive["alive"] = ~alive.churn

        snapshot = alive.copy()
        snapshot["week"] = week
        snapshot["algo"] = algo
        records.append(snapshot)

        alive = alive[alive.alive].copy()

        if len(alive) == 0:
            break

    return pd.concat(records, ignore_index=True)
