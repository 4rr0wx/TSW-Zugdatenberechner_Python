"""Utility functions for train-related calculations."""


def braking_percent(train_weight_t: float, braking_weight_t: float) -> float:
    """Return the braking percentage (Brems Hundertstel) for PZB.

    Args:
        train_weight_t: Total train weight in metric tons.
        braking_weight_t: Total braking weight in metric tons.

    Returns:
        The braking percentage (``BrH``).

    Raises:
        ValueError: If ``train_weight_t`` is not positive or ``braking_weight_t`` is negative.
    """

    if train_weight_t <= 0 or braking_weight_t < 0:
        raise ValueError("Weights must be positive")

    return (braking_weight_t / train_weight_t) * 100

