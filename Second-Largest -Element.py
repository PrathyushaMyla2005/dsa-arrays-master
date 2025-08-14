from typing import List

class ArraySolutions:
    """
    ArraySolutions class contains methods to solve common array problems.
    This includes finding the second largest element using both brute force and optimal approaches.
    """

    # ---------------- Second Largest Element - Brute Force Approach ----------------
    def findSecondLargestBrute(self, nums: List[int]) -> int:
        """
        Brute force approach to find the second largest element in an array.

        Problem:
        Given an array of integers, find the second largest element.

        Approach (Brute Force):
        - Sort the array in descending order.
        - Return the second element (if it exists).

        Time Complexity (TC): O(n log n) --> due to sorting
        Space Complexity (SC): O(n) --> for sorted array

        :param nums: List[int] - list of integers
        :return: int - second largest element
        """
        if len(nums) < 2:
            raise ValueError("Array must have at least 2 elements")

        # Sort in descending order
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[1]  # Second largest element

    # ---------------- Second Largest Element - Optimal Approach ----------------
    def findSecondLargestOptimal(self, nums: List[int]) -> int:
        """
        Optimal approach to find the second largest element in an array.

        Approach (Optimal):
        - Traverse the array once, keeping track of the largest and second largest.
        - Update second largest only when a number is less than the largest but greater than current second largest.

        Time Complexity (TC): O(n) --> single traversal
        Space Complexity (SC): O(1) --> constant space

        :param nums: List[int] - list of integers
        :return: int - second largest element
        """
        if len(nums) < 2:
            raise ValueError("Array must have at least 2 elements")

        largest = second_largest = float('-inf')

        for x in nums:
            if x > largest:
                second_largest = largest
                largest = x
            elif largest > x > second_largest:
                second_largest = x

        if second_largest == float('-inf'):
            raise ValueError("No second largest element found (all elements may be equal)")

        return second_largest


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    solution = ArraySolutions()
    arr = [3, 5, 2, 9, 1]

    # Brute Force
    print("Second largest element (brute force):", solution.findSecondLargestBrute(arr))

    # Optimal
    print("Second largest element (optimal):", solution.findSecondLargestOptimal(arr))
