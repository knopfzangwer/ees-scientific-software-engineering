import numpy as np
import pytest

from ees_scientific_software_engineering.lu_calc import LUSolver


def test_lu_calc():
    mat_A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
    b = np.array([1, 1, 1, 1])
    lusolver = LUSolver(mat_A)
    x = lusolver.solve(b)
    assert np.allclose(mat_A @ x - b, np.zeros((4,))) == True
