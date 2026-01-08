import numpy as np

def love_optimized_score(users, rng):
    """
    Love algorithm:
    High emotional payoff but volatile.
    """
    noise = rng.normal(0, 0.5, size=len(users))
    return (
        1.2 * users["attractiveness"]
        - 0.8 * users["selectiveness"]
        + noise
    )


def retention_optimized_score(users, rng):
    """
    Retention algorithm:
    Stable, predictable, lower variance.
    """
    noise = rng.normal(0, 0.2, size=len(users))
    return (
        0.6 * users["commitment"]
        - 0.3 * users["selectiveness"]
        + noise
    )
