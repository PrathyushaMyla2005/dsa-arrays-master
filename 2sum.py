# File: two_sum_all_approaches.py

def twoSum_bruteforce(nums, target):
    """
    Brute-force approach to find indices of two numbers adding up to target.
    
    Approach:
        - Check all possible pairs using nested loops.
        - Return indices when a valid pair is found.

    Time Complexity: O(n^2)
        - Two nested loops, each iterates over n elements.
    Space Complexity: O(1)
        - No extra space is used.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum_optimized(nums, target):
    """
    Optimized approach using a dictionary (hash map) to find indices of two numbers adding up to target.
    
    Approach:
        - Use a dictionary to store number -> index mapping.
        - For each number, check if (target - num) exists in the dictionary.
        - Return indices immediately when a valid pair is found.

    Time Complexity: O(n)
        - Single pass through the array.
        - Dictionary lookup/insertion is O(1) on average.
    Space Complexity: O(n)
        - Dictionary can store up to n elements.
    
    Why optimized:
        - Brute-force is O(n^2), which is slower for large arrays.
        - Dictionary allows finding the complement in O(1), reducing overall time to O(n).
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i


# Example usage
if __name__ == "__main__":
    arr1 = [2, 7, 11, 15]
    target1 = 9
    print("Array:", arr1)
    print("Target:", target1)
    print("Brute-force result:", twoSum_bruteforce(arr1, target1))
    print("Optimized result:", twoSum_optimized(arr1, target1))

    arr2 = [3, 2, 4]
    target2 = 6
    print("\nArray:", arr2)
    print("Target:", target2)
    print("Brute-force result:", twoSum_bruteforce(arr2, target2))
    print("Optimized result:", twoSum_optimized(arr2, target2))
