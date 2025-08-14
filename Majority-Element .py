# File: majority_element.py

def majorityElement(nums):
    """
    Finds the majority element (> n/2 times) in the array.

    Args:
        nums (list of int): Input array

    Returns:
        int: Majority element
    """
    counts = {}  # Dictionary to store counts

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] > len(nums) // 2:
            return num


# Example usage
if __name__ == "__main__":
    arr1 = [3, 3, 4, 2, 3]
    print("Array:", arr1)
    print("Majority Element:", majorityElement(arr1))

    arr2 = [2, 2, 1, 1, 2]
    print("\nArray:", arr2)
    print("Majority Element:", majorityElement(arr2))
