def fn(arr):
    left = ans = curr = 0

    # for right in range(len(arr)):
    #     # do logic here to add arr[right] to curr

    #     while WINDOW_CONDITION_BROKEN:
    #         # remove arr[left] from curr
    #         left += 1

    #     # update ans
    
    # return ans


# function fn(arr):
#     left = 0
#     for (int right = 0; right < arr.length; right++):
#         Do some logic to "add" element at arr[right] to window

#         while WINDOW_IS_INVALID:
#             Do some logic to "remove" element at arr[left] from window
#             left++

#         Do some logic to update the answer

# function fn(nums, k):
#     left = 0
#     curr = 0
#     answer = 0
#     for (int right = 0; right < nums.length; right++):
#         curr += nums[right]
#         while (curr > k):
#             curr -= nums[left]
#             left++

#         answer = max(answer, right - left + 1)

#     return answer


# FIXED WINDOW

# function fn(arr, k):
#     curr = some data to track the window

#     // build the first window
#     for (int i = 0; i < k; i++)
#         Do something with curr or other variables to build first window

#     ans = answer variable, probably equal to curr here depending on the problem
#     for (int i = k; i < arr.length; i++)
#         Add arr[i] to window
#         Remove arr[i - k] from window
#         Update ans

#     return ans
