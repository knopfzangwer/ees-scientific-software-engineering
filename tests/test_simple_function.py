import numpy as np
import pytest

from ees_scientific_software_engineering.simple_function import add, multiply, rmse


def test_add():
    assert add(1, 1) == 2


def test_multiply():
    assert multiply(2, 2) == 4


def test_add_error():
    a = 1.0
    b = 1
    with pytest.raises(TypeError, match="Arguments should be integers!"):
        add(a, b)


def test_rmse():
    a = np.array([3, 4])
    assert rmse(a) == np.sqrt(12.5)


def test_instance():
    a = 0
    with pytest.raises(TypeError, match="The array should be a instance of np.ndarray!"):
        rmse(a)


def test_rmse_arraylength():
    a = np.array([])
    with pytest.raises(ValueError, match="Array length should not be zero!"):
        rmse(a)


def test_rmse_inf():
    a = np.array([5, np.inf])
    with pytest.raises(ValueError, match="The array should not include inf!"):
        rmse(a)
