#!/usr/bin/python3
"""A module that defines a function called find_peak"""


def find_peak(list_of_integers):
    """
     A function that finds a peak in a list of unsorted integers
    Args:
        list_of_intergers (list): List of integers
    Returns:
        integer of None
    """
    if list_of_integers != []:
        left, right = 0, len(list_of_integers) - 1
        while left < right:
            mid = left + (right-left) // 2
            if list_of_integers[mid] < list_of_integers[mid+1]:
                left = mid + 1
            else:
                right = mid
        return list_of_integers[left]
