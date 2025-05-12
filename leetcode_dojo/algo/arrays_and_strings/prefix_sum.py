def build_prefix_sum(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix

# If we want the sum of the subarray from i to j (inclusive), 
# then the answer is prefix[j] - prefix[i - 1], 
# or alternatively prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

# prefix[j] - prefix[i] + nums[i]