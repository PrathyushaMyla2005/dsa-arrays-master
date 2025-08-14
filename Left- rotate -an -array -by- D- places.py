"""
left_rotate_d.py

Left-rotate an array by D places using the in-place reversal algorithm.


"""

from typing import List

def _reverse_segment(arr: List[int], start: int, end: int) -> None:
    """
    Reverse arr[start..end] in-place (inclusive).

    Parameters
    ----------
    arr : List[int]
        The list of integers to reverse.
    start : int
        Starting index of the segment to reverse.
    end : int
        Ending index of the segment to reverse.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr: List[int], d: int) -> List[int]:
    """
    Left-rotate the list `arr` by `d` positions in-place.

    Parameters
    ----------
    arr : List[int]
        The list to rotate (modified in-place).
    d : int
        Number of left rotations.

    Returns
    -------
    List[int]
        The same list object, rotated.
    """
    n = len(arr)
    if n == 0:
        return arr  # nothing to do

    # Normalize d (ensure 0 <= d < n)
    d = d % n
    if d == 0:
        return arr  # already effectively rotated by 0

    # Step 1: reverse first d elements
    _reverse_segment(arr, 0, d - 1)

    # Step 2: reverse remaining n-d elements
    _reverse_segment(arr, d, n - 1)

    # Step 3: reverse the whole array
    _reverse_segment(arr, 0, n - 1)

    return arr


if __name__ == "__main__":
    # Example usage
    example = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    print("Original:", example)
    left_rotate(example, d)
    print(f"Left rotated by {d}:", example)
