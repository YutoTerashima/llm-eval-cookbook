from __future__ import annotations

import random


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def bootstrap_ci(values: list[float], samples: int = 200, seed: int = 7) -> tuple[float, float]:
    if not values:
        return (0.0, 0.0)
    rng = random.Random(seed)
    estimates = []
    for _ in range(samples):
        draw = [rng.choice(values) for _ in values]
        estimates.append(mean(draw))
    estimates.sort()
    lo = estimates[int(0.025 * (samples - 1))]
    hi = estimates[int(0.975 * (samples - 1))]
    return (round(lo, 3), round(hi, 3))
