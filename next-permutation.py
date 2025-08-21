import itertools

def nextPermutation(nums):
    # Step 1: Generate all permutations
    perms = sorted(set(itertools.permutations(nums)))
    
    # Step 2: Find current index
    idx = perms.index(tuple(nums))
    
    # Step 3: Return next permutation (or first if last)
    return list(perms[(idx + 1) % len(perms)])


# -------------------- Examples --------------------

# Example 1
print(nextPermutation([1,2,3]))  
# perms = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
# current = (1,2,3) at index 0
# next = (1,3,2)
# Output → [1,3,2]

# Example 2
print(nextPermutation([3,2,1]))  
# perms = [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]
# current = (3,2,1) at index 5
# next = wrap around → (1,2,3)
# Output → [1,2,3]

# Example 3
print(nextPermutation([1,1,5]))  
# perms = [(1,1,5),(1,5,1),(5,1,1)]
# current = (1,1,5) at index 0
# next = (1,5,1)
# Output → [1,5,1]
def nextPermutation(nums):
    # nums = [1,1,5]

    # Step 1: Find the pivot
    i = len(nums) - 2        # i = 1 (nums[1] = 1)
    while i >= 0 and nums[i] >= nums[i + 1]:
        # nums[1]=1 < nums[2]=5 → false → stop
        # Pivot found at index 1 (value 1)
        i -= 1

    # Step 2: Pivot exists
    if i >= 0:               # i = 1
        j = len(nums) - 1    # j = 2 (nums[2] = 5)
        while nums[j] <= nums[i]:
            # nums[2]=5 > nums[1]=1 → false → stop
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # Swap nums[1]=1 with nums[2]=5
        # nums = [1,5,1]

    # Step 3: Reverse suffix (after index 1)
    nums[i + 1:] = reversed(nums[i + 1:])
    # nums[2:] = reversed([1]) → [1]
    # nums = [1,5,1]

    return nums
print(nextPermutation([1,1,5]))