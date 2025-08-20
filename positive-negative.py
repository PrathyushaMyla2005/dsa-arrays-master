'''✅ Approach 1: Extra Space (Two Arrays)

👉 Simple & clear method (O(n) time, O(n) space). Good for beginners.

Steps:

Separate positives and negatives into two arrays.

Alternate pick from positives and negatives.

If one list is longer, append remaining elements at the end.'''
def rearrange_alternate(arr):
    pos = []
    neg = []
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    result = []
    i = j = 0

    # Alternate between pos and neg
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    # Add remaining positives
    while i < len(pos):
        result.append(pos[i])
        i += 1   # ✅ increment i

    # Add remaining negatives
    while j < len(neg):
        result.append(neg[j])
        j += 1   # ✅ increment j

    return result


arr = [1,4,5,-2,-4,1,-3,2,3,-5]
print("Extra Space:", rearrange_alternate(arr))
'''Time Complexity

Separation: O(n)

Alternating placement: O(n)

Extending leftovers: O(n) (but more efficient than looping)

✅ Overall → O(n)

Space Complexity

Same as Approach 1 → pos + neg + result → O(n)

✅ Overall → O(n)
✅ Approach 2: In-Place (Two Pointers)
👉 More efficient (O(n) time, O(1) space). Good for intermediate level.
Steps:
Use two pointers to track positions of positives and negatives.
Swap elements in-place to alternate them.
'''
def rearrange_two_pointers(arr):
    # Step 1: Separate positives and negatives
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]

    # Step 2: Create result array
    result = []
    i = j = 0

    # Step 3: Alternate placement
    while i < len(pos) and j < len(neg):
        result.append(pos[i])   # place positive
        result.append(neg[j])   # place negative
        i += 1
        j += 1

    # Step 4: Add leftovers
    result.extend(pos[i:])
    result.extend(neg[j:])

    return result
arr = [1,4,5,-2,-4,1,-3,2,3,-5]
print("Extra Space:", rearrange_two_pointers(arr))
