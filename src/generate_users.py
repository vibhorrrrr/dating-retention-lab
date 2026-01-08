import numpy as np
import pandas as pd

def generate_users(n_users=2000, seed=42):
    rng = np.random.default_rng(seed)

    users = pd.DataFrame({
        "user_id": range(n_users),
        "attractiveness": rng.normal(0, 1, n_users),
        "selectiveness": rng.uniform(0.3, 0.9, n_users),
        "commitment": rng.uniform(0.2, 1.0, n_users),
        "churn_base": rng.uniform(0.01, 0.05, n_users)
    })

    return users
