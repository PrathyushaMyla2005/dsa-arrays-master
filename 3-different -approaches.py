from itertools import permutations

def nextPermutation_bruteforce(nums):
    # Step 1: Generate all unique permutations
    perms = sorted(set(permutations(nums)))
    
    # Step 2: Find current position
    idx = perms.index(tuple(nums))
    
    # Step 3: Return next permutation or wrap to first
    next_perm = perms[(idx + 1) % len(perms)]
    return list(next_perm)


# Example
print("Brute Force:", nextPermutation_bruteforce([1,2,3]))  # [1,3,2]
print("Brute Force:", nextPermutation_bruteforce([3,2,1]))  # [1,2,3]

def nextPermutation_optimal(nums):
    n = len(nums)
    
    # Step 1: Find first decreasing element
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find just larger element
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse suffix
    nums[i+1:] = reversed(nums[i+1:])
    return nums


# Example
print("Optimal:", nextPermutation_optimal([1,2,3]))  # [1,3,2]
print("Optimal:", nextPermutation_optimal([3,2,1]))  # [1,2,3]
