"""LU decomposition and solve a linear equation

Returns:
    a numpy ndarray
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve

class LUSolver:
    """_summary_
    """
    def __init__(self, input_matrix: np.ndarray):
        """
        Constructor of the class. It takes the input matrix and decompose it into LU factorization.
        Store the factorization and permutation into class members.
        """
        lu, piv = lu_factor(input_matrix)
        self.lu = lu
        self.piv = piv


    def solve(self, b: np.ndarray) -> np.ndarray:
        """
        Solve the linear equation with the input matrix and the given vector b.
        """
        x = lu_solve((self.lu, self.piv), b)
        return x
