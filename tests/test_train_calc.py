from train_calc import braking_percent


def test_braking_percent() -> None:
    """BrH for 256 t braking weight and 400 t train weight should be 64."""
    assert braking_percent(400, 256) == 64

