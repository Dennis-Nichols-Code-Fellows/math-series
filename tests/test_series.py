from series import *


def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_input_0():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected, f"Bad result for fibonacci(0). Expected: {expected}, Actual: {actual}"


def test_fibonacci_input_1():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected, f"Bad result for fibonacci(1). Expected: {expected}, Actual: {actual}"


def test_fibonacci_input_2():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected, f"Bad result for fibonacci(2). Expected: {expected}, Actual: {actual}"


def test_fibonacci_input_a():
    """
    :return: tests if fib returns None for anything that isn't a number.
    """
    expected = None
    actual = fibonacci('a')
    assert actual == expected, f"Bad result for fibonacci('a'). Expected: {expected}, Actual: {actual}"


def test_lucas_exists():
    assert lucas


def test_lucas_input_0():
    expected = 2
    actual = lucas(0)
    assert actual == expected, f"Bad result for lucas(0). Expected: {expected}, Actual: {actual}"


def test_lucas_input_1():
    expected = 1
    actual = lucas(1)
    assert actual == expected, f"Bad result for lucas(1). Expected: {expected}, Actual: {actual}"


def test_lucas_input_2():
    expected = 3
    actual = lucas(2)
    assert actual == expected, f"Bad result for lucas(2). Expected: {expected}, Actual: {actual}"


def test_lucas_input_a():
    """
    :return: tests if lucas returns None for anything that isn't a number.
    """
    expected = None
    actual = lucas('a')
    assert actual == expected, f"Bad result for fibonacci('a'). Expected: {expected}, Actual: {actual}"


def test_series_input_2_default():
    expected = 1
    actual = series(2)
    assert actual == expected, f"Bad result for series(2). Expected: {expected}, Actual: {actual}"


def test_series_input_2_with_optional_lucas_numbers():
    expected = 3
    actual = series(2, 2, 1)
    assert actual == expected, f"Bad result for series(2). Expected: {expected}, Actual: {actual}"