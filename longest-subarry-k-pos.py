def longest_subarray_with_sum_k(arr, K):
    """
    Finds the length of the longest subarray with sum exactly equal to K.
    
    Parameters:
    arr (list): List of positive integers
    K (int): Target sum
    
    Returns:
    int: Length of the longest subarray with sum = K
    """
    
    start = 0  # Left boundary of window
    current_sum = 0  # Sum of current window
    max_length = 0  # Store longest length found
    
    # Loop through the array with `end` pointer
    for end in range(len(arr)):
        current_sum += arr[end]  # Add current element to the sum
        
        # Shrink the window from the left if sum exceeds K
        while current_sum > K:
            current_sum -= arr[start]
            start += 1
        
        # If sum is exactly K, update max_length
        if current_sum == K:
            window_length = end - start + 1
            max_length = max(max_length, window_length)
    
    return max_length


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 1, 1, 1, 3, 2]
    K = 5
    result = longest_subarray_with_sum_k(arr, K)
    print("Length of the longest subarray:", result)
