#!/usr/bin/python3

"""
TODO:
    * Write a function that multiplies 2 matrices using a module called NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Use NumPy to multiply mattices

    Args:
        m_a (list of lists): contains integer/floats
        m_b (list of lists): contains integer/floats

    Returns:
        lists
    """
    return np.matmul(m_a, m_b)
