from typing import List

class ArraySolutions:
    """
    ArraySolutions class contains methods to solve common array problems.
    This includes finding the missing number in an array containing distinct numbers from 1 to n.
    """

    # ---------------- Missing Number - Sum Formula Approach ----------------
    def findMissingNumberSum(self, nums: List[int]) -> int:
        """
        Finds the missing number using the sum formula for the first n natural numbers.

        Problem:
        Given an array of size n containing distinct integers from 1 to n+1 with exactly one missing number,
        find and return the missing number.

        Approach (Sum Formula):
        - Calculate the expected sum of numbers from 1 to n+1 using the formula: total = n*(n+1)/2
        - Find the actual sum of elements in the array.
        - The difference between expected sum and actual sum is the missing number.

        Time Complexity (TC): O(n) --> single traversal to calculate actual sum
        Space Complexity (SC): O(1) --> no extra space used

        :param nums: List[int] - list containing numbers from 1 to n+1 with one missing
        :return: int - missing number
        """
        n = len(nums) + 1  # Since one number is missing
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # ---------------- Missing Number - XOR Approach ----------------
    def findMissingNumberXOR(self, nums: List[int]) -> int:
        """
        Finds the missing number using the XOR method.

        Approach (XOR):
        - XOR all numbers from 1 to n+1 (call it xor_all).
        - XOR all elements present in the array (call it xor_array).
        - Missing number = xor_all ^ xor_array (because XOR cancels matching numbers).

        Time Complexity (TC): O(n) --> two traversals
        Space Complexity (SC): O(1) --> no extra space used

        :param nums: List[int] - list containing numbers from 1 to n+1 with one missing
        :return: int - missing number
        """
        n = len(nums) + 1
        xor_all = 0
        xor_array = 0

        for i in range(1, n + 1):
            xor_all ^= i

        for num in nums:
            xor_array ^= num

        return xor_all ^ xor_array


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    solution = ArraySolutions()

    arr = [1, 2, 4, 5]  # Missing number is 3

    # Sum formula approach
    print("Missing Number (Sum formula):", solution.findMissingNumberSum(arr))

    # XOR approach
    print("Missing Number (XOR):", solution.findMissingNumberXOR(arr))
