from src.funcs import divide


def test_divide():
    assert divide(10, 5) == 2
    assert divide(6.6, 2) == 3.3
    assert divide(6, 1) == 6


def test_divide_zero():
    pass
