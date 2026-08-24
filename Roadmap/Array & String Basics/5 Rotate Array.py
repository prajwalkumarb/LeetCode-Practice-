# 5. Rotate Array
# Problem: Given an array nums, rotate the array to the right by k steps, where k is non-negative. Do this in-place.

# Example:
# Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]

# Explanation: rotating right by 1 step moves the last element to the front:
# [1,2,3,4,5,6,7] → rotate 1 → [7,1,2,3,4,5,6]
#                 → rotate 2 → [6,7,1,2,3,4,5]
#                 → rotate 3 → [5,6,7,1,2,3,4]
# Think about it: A brute-force way is to rotate one step at a time, k times — but that's O(n·k), slow for large k.


# split list into 2 parts
def rotate_array(nums,k):
    list1 = nums[:-k]
    list2 = nums[-k:]
    return list2 + list1    
    
def rotate_array_1(nums,k):
    n = len(nums)
    k = k % n
    a = list(reversed(nums[:k+1]))
    print(a)
    b = list(reversed(nums[-k:]))
    print(b)
    a.extend(b)
    nums = list(reversed(a))
    return nums
    
def rotate_array_2(nums,k):
    n = len(nums)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            nums[start] , nums[end] = nums[end] , nums[start]
            start +=1
            end  -=1
    reverse(0,len(nums)-k-1)
    reverse(len(nums)-k,len(nums)-1)
    reverse(0,len(nums)-1)
    return nums

if __name__ == "__main__":
    result = rotate_array(nums = [1, 2, 3, 4, 5, 6, 7], k = 3)
    print(result)
    
    result_1 = rotate_array_1(nums=[1, 2, 3, 4, 5, 6, 7], k = 3)
    print(result_1)
    
    result_3 = rotate_array_2(nums=[1, 2, 3, 4, 5, 6, 7], k = 3)
    print(result_3)