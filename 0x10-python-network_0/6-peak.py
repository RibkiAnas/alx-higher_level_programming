#!/usr/bin/python3
"""
Function that finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of unsorted integers
    Returns: a peak in a list of unsorted integers or None
    """

    if not list_of_integers:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    """Use binary search to find a peak"""
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        """find the middle index"""
        mid = (left + right) // 2

        """
        Compare the middle elm with its neighbors
        if the middle elm is smaller than the
        right neighbor, move the left pointer
        to the right of the middle
        """
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
