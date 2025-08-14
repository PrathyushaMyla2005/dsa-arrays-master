from typing import List

class ArraySolutions:
    """
    ArraySolutions class contains methods to solve common array problems.
    This includes moving all zeros in an array to the end while maintaining the order of non-zero elements.
    """

    # ---------------- Move Zeros to End - Brute Force Approach ----------------
    def moveZerosBrute(self, nums: List[int]) -> List[int]:
        """
        Brute force approach to move all zeros to the end of the array.

        Problem:
        Given an array, move all zeros to the end while keeping the relative order of non-zero elements.

        Approach (Brute Force):
        - Create a new list with all non-zero elements first.
        - Append the required number of zeros at the end.
        - Return the new list.

        Time Complexity (TC): O(n) --> traverses list twice (non-zeros + zeros)
        Space Complexity (SC): O(n) --> extra list for storing result

        :param nums: List[int] - list of integers
        :return: List[int] - new list with zeros at the end
        """
        non_zero_elements = [x for x in nums if x != 0]  # Collect all non-zero elements
        zero_count = nums.count(0)  # Count total zeros
        return non_zero_elements + [0] * zero_count  # Append zeros at end

    # ---------------- Move Zeros to End - Optimal Approach ----------------
    def moveZerosOptimal(self, nums: List[int]) -> None:
        """
        Optimal in-place approach to move all zeros to the end of the array.

        Approach (Optimal):
        - Use a pointer `insert_pos` to track the position to place the next non-zero element.
        - Traverse the array and place each non-zero element at `insert_pos`.
        - After traversal, fill the rest with zeros.
        - Works in-place, no extra array.

        Time Complexity (TC): O(n) --> single traversal
        Space Complexity (SC): O(1) --> in-place

        :param nums: List[int] - list of integers (modified in place)
        :return: None
        """
        insert_pos = 0  # Position to insert next non-zero element

        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Fill remaining positions with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    solution = ArraySolutions()

    arr = [0, 1, 0, 3, 12]

    # Brute Force
    print("Move Zeros (brute force):", solution.moveZerosBrute(arr))

    # Optimal
    arr_optimal = [0, 1, 0, 3, 12]
    solution.moveZerosOptimal(arr_optimal)
    print("Move Zeros (optimal, in-place):", arr_optimal)
