"""
Find the element that appears exactly once in a list where all other elements appear twice.
Uses the XOR approach for O(n) time and O(1) space.
"""

from typing import List

def single_number(nums: List[int]) -> int:
    """
    Returns the element that appears exactly once in the given list.
    
    Args:
        nums (List[int]): A list of integers where every element appears twice except one.
    
    Returns:
        int: The element that appears only once.
    """
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out duplicates and leaves the unique element
    return result


if __name__ == "__main__":
    # Example usage
    numbers = [4, 1, 2, 1, 2]
    print(f"The single number is: {single_number(numbers)}")
