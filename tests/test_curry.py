import pytest
from hypothesis import given
from hypothesis import strategies as st

from functions_curry_7.curry_uncurry import curry, uncurry

# unit тесты


def test_curry_basic():
    """Тест каррирования функции с 3 аргументами."""

    def sum_3(a, b, c):
        return a + b + c

    curried = curry(sum_3, 3)
    result = curried(1)(2)(3)
    assert result == 6, f"Ожидалось 6, получено {result}"


def test_curry_partial_application():
    """Тест частичного применения каррированной функции."""

    def multiply(a, b):
        return a * b

    curried = curry(multiply, 2)
    double = curried(2)

    assert double(5) == 10
    assert double(6) == 12
    assert callable(double), "Частично примененная функция должна быть вызываемой"


def test_uncurry_basic():
    """Тест обратимости"""

    def add_4(a, b, c, d):
        return a + b + c + d

    curried = curry(add_4, 4)
    uncurried = uncurry(curried, 4)

    assert curried(1)(2)(3)(4) == 10
    assert uncurried(1, 2, 3, 4) == 10


def test_zero_arity():
    """Тестирование функций с нулевой арностью"""

    def constant():
        return 42

    curried_const = curry(constant, 0)
    assert curried_const() == 42

    uncurried_const = uncurry(curried_const, 0)
    assert uncurried_const() == 42


def test_single_argument():
    """Тестирование функций с одним аргументом"""

    def identity(x):
        return x

    curried_id = curry(identity, 1)
    assert curried_id(5) == 5

    uncurried_id = uncurry(curried_id, 1)
    assert uncurried_id(10) == 10


# тесты ошибок


def test_curry_negative_arity():
    """Тест ошибки при отрицательной арности в curry."""

    def func(a):
        return a

    with pytest.raises(ValueError, match="Арность не должна быть <0"):
        curry(func, -1)

    with pytest.raises(ValueError, match="Арность не должна быть <0"):
        curry(func, -100)


def test_uncurry_negative_arity():
    """Тест ошибки при отрицательной арности в uncurry."""

    def func(a):
        return a

    curried = curry(func, 1)

    with pytest.raises(ValueError, match="Арность не должна быть <0"):
        uncurry(curried, -1)


def test_uncurry_wrong_number_of_args():
    """Тест ошибки при передаче неправильного количества аргументов в uncurry."""

    def sum_3(a, b, c):
        return a + b + c

    curried = curry(sum_3, 3)
    uncurried = uncurry(curried, 3)

    with pytest.raises(TypeError, match="Функция ожидает 3 аргументов"):
        uncurried(1, 2)

    with pytest.raises(TypeError, match="Функция ожидает 3 аргументов"):
        uncurried(1, 2, 3, 4)


# Property-based тесты с hypothesis

integers = st.integers(min_value=-100, max_value=100)
small_lists = st.lists(integers, min_size=0, max_size=5)


@given(a=integers, b=integers, c=integers)
def test_curry_uncurry_inverse(a: int, b: int, c: int):
    """
    Property-based тест: curry и uncurry обратны друг другу.
    Для любых a, b, c результаты должны совпадать.
    """

    def sum_3(x, y, z):
        return x + y + z

    curried = curry(sum_3, 3)
    uncurried = uncurry(curried, 3)

    assert curried(a)(b)(c) == uncurried(a, b, c)
    assert curried(a)(b)(c) == a + b + c


@given(args=st.tuples(integers, integers, integers))
def test_curry_preserves_behavior(args):
    """
    Property-based тест: каррированная функция ведет себя так же,
    как исходная.
    """

    def sum_3(x, y, z):
        return x + y + z

    curried = curry(sum_3, 3)
    a, b, c = args

    direct_result = sum_3(a, b, c)
    curried_result = curried(a)(b)(c)

    assert direct_result == curried_result


@given(x=integers, y=integers, z=integers, w=integers)
def test_partial_application_property(x, y, z, w):
    """
    Property-based тест: частичное применение работает корректно.
    """

    def add4(a, b, c, d):
        return a + b + c + d

    curried_add4 = curry(add4, 4)
    partially_applied = curried_add4(x)(y)

    assert callable(partially_applied)

    result = partially_applied(z)(w)

    assert result == x + y + z + w
    assert result == add4(x, y, z, w)
