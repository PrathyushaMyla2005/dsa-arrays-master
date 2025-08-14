from typing import List, Any

class ArraySolutions:
    """
    ArraySolutions class contains methods to solve common array problems.
    This includes performing Linear Search to find an element in an array.
    """

    # ---------------- Linear Search - Iterative Approach ----------------
    def linearSearchIterative(self, nums: List[Any], target: Any) -> int:
        """
        Iterative approach to find the index of the target element in the array.

        Problem:
        Given an array and a target value, return the index of the first occurrence of the target.
        If the target is not found, return -1.

        Approach (Iterative):
        - Traverse the array from left to right.
        - Compare each element with the target.
        - If found, return its index immediately.
        - If loop ends without match, return -1.

        Time Complexity (TC): O(n) --> traverses at most the entire array
        Space Complexity (SC): O(1) --> no extra space used

        :param nums: List[Any] - list of elements
        :param target: Any - element to search for
        :return: int - index of target or -1 if not found
        """
        for index, value in enumerate(nums):
            if value == target:
                return index  # Found target
        return -1  # Target not found

    # ---------------- Linear Search - Recursive Approach ----------------
    def linearSearchRecursive(self, nums: List[Any], target: Any, index: int = 0) -> int:
        """
        Recursive approach to find the index of the target element in the array.

        Approach (Recursive):
        - Base Case: If index reaches the end of the array, return -1.
        - If nums[index] matches target, return index.
        - Else, call the function again with index + 1.

        Time Complexity (TC): O(n) --> visits each element once
        Space Complexity (SC): O(n) --> due to recursion call stack

        :param nums: List[Any] - list of elements
        :param target: Any - element to search for
        :param index: int - current index in recursion
        :return: int - index of target or -1 if not found
        """
        if index >= len(nums):  # Base case: end of array
            return -1
        if nums[index] == target:
            return index
        return self.linearSearchRecursive(nums, target, index + 1)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    solution = ArraySolutions()

    arr = [4, 2, 7, 1, 9]

    # Iterative
    target = 7
    print(f"Linear Search (iterative) - Index of {target}:", solution.linearSearchIterative(arr, target))

    # Recursive
    target = 1
    print(f"Linear Search (recursive) - Index of {target}:", solution.linearSearchRecursive(arr, target))

    # Not found
    target = 5
    print(f"Linear Search (iterative) - Index of {target}:", solution.linearSearchIterative(arr, target))
