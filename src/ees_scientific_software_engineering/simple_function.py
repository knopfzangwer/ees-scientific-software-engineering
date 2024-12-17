"""
A module with simple function
"""

import numpy as np


def add(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a: number a
        b: number b

    Returns:
        added number
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments should be integers!")
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


def rmse(input_array: np.ndarray) -> float:
    """Calculate root mean square

    Args:
        input_array: array

    Raises:
        TypeError: _description_
        ValueError: _description_

    Returns:
        _description_
    """
    if not isinstance(input_array, np.ndarray):
        raise TypeError("The array should be a instance of np.ndarray!")
    if len(input_array) == 0:
        raise ValueError("Array length should not be zero!")
    if len(input_array.shape) > 1:
        raise TypeError("The shape of the array must be one-dimensional!")
    if np.inf in input_array:
        raise ValueError("The array should not include inf!")
    if np.any(np.isnan(input_array)):
        raise ValueError("The array should not include NaN!")
    if input_array.dtype != np.float64:
        raise ValueError("The type of the array must be float64!")
    return np.sqrt(np.mean((input_array**2)))
