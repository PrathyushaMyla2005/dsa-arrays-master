# File: sort_012_all_approaches.py

def sort012_count(nums):
    """
    Brute-force / count approach to sort 0s, 1s, and 2s in-place.
    
    Approach:
        - Count the number of 0s, 1s, and 2s in the array.
        - Overwrite the array with correct number of 0s, then 1s, then 2s.

    Time Complexity: O(n)
        - Traverse the array twice: once for counting, once for overwriting.
    Space Complexity: O(1)
        - Only counters are used, no extra array.
    """
    count0 = count1 = count2 = 0

    # Count 0s, 1s, and 2s
    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    # Overwrite the array based on counts
    i = 0
    for _ in range(count0):
        nums[i] = 0
        i += 1
    for _ in range(count1):
        nums[i] = 1
        i += 1
    for _ in range(count2):
        nums[i] = 2
        i += 1


def sort012_dnf(nums):
    """
    Optimized Dutch National Flag approach to sort 0s, 1s, 2s in-place.

    Approach:
        - Use three pointers: low, mid, high.
        - low -> next position for 0
        - mid -> current element
        - high -> next position for 2
        - Swap elements to correct positions in a single pass.

    Time Complexity: O(n)
        - Single traversal of the array.
    Space Complexity: O(1)
        - In-place sorting, no extra space.
    
    Why optimized:
        - Only one pass through array vs counting method which traverses twice.
        - Constant space, in-place swaps.
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Example usage
if __name__ == "__main__":
    arr1 = [2, 0, 2, 1, 1, 0]
    print("Original Array:", arr1)
    
    # Brute-force / count approach
    arr1_count = arr1.copy()
    sort012_count(arr1_count)
    print("Count Approach Sorted:", arr1_count)
    
    # Optimized Dutch National Flag approach
    arr1_dnf = arr1.copy()
    sort012_dnf(arr1_dnf)
    print("Dutch National Flag Sorted:", arr1_dnf)

    arr2 = [0, 2, 1, 0, 2, 1, 1, 0]
    print("\nOriginal Array:", arr2)
    
    arr2_count = arr2.copy()
    sort012_count(arr2_count)
    print("Count Approach Sorted:", arr2_count)
    
    arr2_dnf = arr2.copy()
    sort012_dnf(arr2_dnf)
    print("Dutch National Flag Sorted:", arr2_dnf)
