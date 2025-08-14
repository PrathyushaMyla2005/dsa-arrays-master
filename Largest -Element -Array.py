from typing import List

class ArraySolutions:
    """
    ArraySolutions class contains methods to solve common array problems.
    This includes finding the largest element using both brute force and optimal approaches.
    """

    # ---------------- Largest Element - Brute Force Approach ----------------
    def findLargestBrute(self, nums: List[int]) -> int:
        """
        Brute force approach to find the largest element in an array.

        Problem:
        Given an array of integers, find the largest element.

        Approach (Brute Force):
        - Compare each element with all other elements in the array.
        - If no other element is larger, it is the largest.

        Time Complexity (TC): O(n^2) --> nested loops
        Space Complexity (SC): O(1) --> constant space

        :param nums: List[int] - list of integers
        :return: int - largest element
        """
        if not nums:
            raise ValueError("Array is empty")  # Edge case handling

        n = len(nums)
        max_val = nums[0]

        for i in range(n):
            is_largest = True
            for j in range(n):
                if nums[j] > nums[i]:
                    is_largest = False
                    break
            if is_largest:
                max_val = nums[i]

        return max_val

    # ---------------- Largest Element - Optimal Approach ----------------
    def findLargestOptimal(self, nums: List[int]) -> int:
        """
        Optimal approach to find the largest element in an array.

        Approach (Optimal):
        - Initialize max_val as the first element.
        - Traverse the array once, updating max_val if a larger element is found.

        Time Complexity (TC): O(n) --> single traversal
        Space Complexity (SC): O(1) --> constant space

        :param nums: List[int] - list of integers
        :return: int - largest element
        """
        if not nums:
            raise ValueError("Array is empty")

        max_val = nums[0]

        for x in nums:
            if x > max_val:
                max_val = x

        return max_val


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    solution = ArraySolutions()
    arr = [3, 5, 2, 9, 1]

    # Brute Force
    print("Largest element (brute force):", solution.findLargestBrute(arr))

    # Optimal
    print("Largest element (optimal):", solution.findLargestOptimal(arr))
