#!/usr/bin/python3

"""
A function that multiplies two matrices
"""


def outterListCheck(m_a, m_b):
    """
    Checks if both arguments are lists

    Args:
        m_a (list)
        m_b (list)
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')


def isOutterListEmpty(m_a, m_b):
    """
    Checks if outter list is empty

    Args:
        m_a (list)
        m_b (list)
    """
    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0:
        raise ValueError('m_b can\'t be empty')


def isListOfLists(m_a, m_b):
    """
    Checks if arguments are list of lists

    Args:
        m_a (list)
        m_b (list)
    """
    if not all(map(lambda x: type(x) == list, m_a)):
        raise TypeError('m_a must be a list of lists')
    if not all(map(lambda x: type(x) == list, m_b)):
        raise TypeError('m_b must be a list of lists')


def isInnerListEmpty(m_a, m_b):
    """
    Checks if inner lists are empty

    Args:
        m_a (list)
        m_b (list)
    """
    if len(m_a) == 1 or len(m_b) == 1:
        if len(m_a[0]) == 0:
            raise ValueError('m_a can\'t be empty')
        if len(m_b[0]) == 0:
            raise ValueError('m_b can\'t be empty')


def integersAndFloats(m_a, m_b):
    """
    Checks if both list contains integers or floats

    Args:
        m_a (list)
        m_b (list)
    """
    for row in m_a:
        if not all(map(lambda x: isinstance(x, (int, float)), row)):
            raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        if not all(map(lambda x: isinstance(x, (int, float)), row)):
            raise TypeError('m_b should contain only integers or floats')


def checkRowSize(m_a, m_b):
    """
    Checks to ensure all rows are same

    Args:
        m_a (list)
        m_b (list)
    """
    if not all(map(lambda x: len(x) == len(m_a[0]), m_a)):
        raise TypeError('each row of m_a must be of the same size')
    if not all(map(lambda x: len(x) == len(m_b[0]), m_b)):
        raise TypeError('each row of m_b must be of the same size')


def matrix_mul(m_a, m_b):
    """
    Multiply matrix m_a and m_b

    Args:
        m_a (list)
        m_b (list)

    Returns:
        matrix (list)
    """
    outterListCheck(m_a, m_b)
    isOutterListEmpty(m_a, m_b)
    isListOfLists(m_a, m_b)
    isInnerListEmpty(m_a, m_b)
    integersAndFloats(m_a, m_b)
    checkRowSize(m_a, m_b)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    product = []
    for row in m_a:
        new = []
        for x in range(len(m_b[0])):
            result = 0
            for y in range(len(m_b)):
                result += row[y] * m_b[y][x]
            new.append(result)
        product.append(new)
    return product
