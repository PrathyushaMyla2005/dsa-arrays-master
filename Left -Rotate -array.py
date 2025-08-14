from typing import List

class ArraySolutions:
    """
    ArraySolutions class contains methods to solve common array problems.
    This includes checking if an array is sorted using both brute force and optimal approaches.
    """

    # ---------------- Check if Array is Sorted - Brute Force Approach ----------------
    def isSortedBrute(self, nums: List[int]) -> bool:
        """
        Brute force approach to check if the array is sorted in non-decreasing order.

        Problem:
        Given an array of integers, determine if it is sorted in non-decreasing order.

        Approach (Brute Force):
        - Create a sorted copy of the array.
        - Compare it with the original.
        - If both are the same, array is sorted.

        Time Complexity (TC): O(n log n) --> due to sorting
        Space Complexity (SC): O(n) --> for the sorted copy

        :param nums: List[int] - list of integers
        :return: bool - True if sorted, False otherwise
        """
        return nums == sorted(nums)

    # ---------------- Check if Array is Sorted - Optimal Approach ----------------
    def isSortedOptimal(self, nums: List[int]) -> bool:
        """
        Optimal approach to check if the array is sorted in non-decreasing order.

        Approach (Optimal):
        - Traverse the array once.
        - Compare each element with the previous one.
        - If any element is smaller than the previous, return False.

        Time Complexity (TC): O(n) --> single traversal
        Space Complexity (SC): O(1) --> constant space

        :param nums: List[int] - list of integers
        :return: bool - True if sorted, False otherwise
        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:  # Found a decreasing pair
                return False
        return True


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    solution = ArraySolutions()

    arr_sorted = [1, 2, 3, 4, 5]
    arr_unsorted = [3, 1, 4, 2]

    # Brute Force
    print("Is sorted (brute force) - sorted array:", solution.isSortedBrute(arr_sorted))
    print("Is sorted (brute force) - unsorted array:", solution.isSortedBrute(arr_unsorted))

    # Optimal
    print("Is sorted (optimal) - sorted array:", solution.isSortedOptimal(arr_sorted))
    print("Is sorted (optimal) - unsorted array:", solution.isSortedOptimal(arr_unsorted))
