"""
check_sorted.py

A simple Python script to check if a list is sorted in ascending order.
"""

def is_sorted(arr):
    """
    Check if the given list is sorted in ascending order.

    Parameters
    ----------
    arr : list
        The list of comparable elements (numbers, strings, etc.).

    Returns
    -------
    bool
        True if the list is sorted in ascending order, False otherwise.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    # Example usage
    example1 = [1, 2, 3, 4, 5]
    example2 = [1, 3, 2, 4, 5]

    print(f"Example 1: {example1} → Sorted? {is_sorted(example1)}")
    print(f"Example 2: {example2} → Sorted? {is_sorted(example2)}")
