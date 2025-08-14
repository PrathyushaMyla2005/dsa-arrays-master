from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Given a binary array nums, return the maximum number
        of consecutive 1's in the array.

        :param nums: List[int] - list containing only 0s and 1s
        :return: int - length of the longest consecutive 1s
        """
        max_run = 0   # Longest streak of 1s found so far
        current = 0   # Current streak length

        for x in nums:
            if x == 1:
                current += 1
                max_run = max(max_run, current)
            else:
                current = 0

        return max_run


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    example_nums = [1, 1, 0, 1, 1, 1]
    print("Maximum consecutive 1s:", solution.findMaxConsecutiveOnes(example_nums))
