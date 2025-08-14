def max_subarray_brute(nums):
    """
    Brute-force approach: find maximum sum by checking all subarrays.
    Returns both maximum sum and subarray itself.
    """
    n = len(nums)
    max_sum = float('-inf')  # Initialize max sum
    start = 0
    end = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]  # Sum of subarray nums[i..j]
            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j

    return max_sum, nums[start:end+1]


def max_subarray_kadane(nums):
    """
    Kadane's Algorithm: find maximum sum in O(n) time.
    Returns both maximum sum and subarray itself.
    """
    current_sum = 0
    max_sum = float('-inf')
    start = end = temp_start = 0

    for i, num in enumerate(nums):
        current_sum += num  # Add current element to running sum

        if current_sum > max_sum:  # Update max sum and indices
            max_sum = current_sum
            start = temp_start
            end = i

        if current_sum < 0:  # Reset if running sum is negative
            current_sum = 0
            temp_start = i + 1

    return max_sum, nums[start:end+1]


# ----------------- Example Usage -----------------
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Brute-force result
    brute_sum, brute_subarray = max_subarray_brute(nums)
    print("Brute-Force Result:")
    print("Maximum Sum:", brute_sum)
    print("Subarray:", brute_subarray)
    print()

    # Kadane's Algorithm result
    kadane_sum, kadane_subarray = max_subarray_kadane(nums)
    print("Kadane's Algorithm Result:")
    print("Maximum Sum:", kadane_sum)
    print("Subarray:", kadane_subarray)
