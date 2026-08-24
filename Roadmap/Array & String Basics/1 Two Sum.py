# 1. Two Sum
# Problem: Given an array of integers nums and an integer target, 
#           return the indices of the two numbers that add up to target. 
#           You may assume each input has exactly one solution, 
#           and you can't use the same element twice.


# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]   // because nums[0] + nums[1] == 9
# Take a shot at it — how would you approach this? If you want, 
# just tell me your idea in words first (brute force vs. optimized), 
# or write out actual code. I'll give feedback either way.


def two_sum(nums,targer):
    mapper = {}
    for ind , val in enumerate(nums):
        rem_val = targer - val
        if rem_val in  mapper:
            return [mapper[rem_val], ind]
        
        mapper[val] = ind
    
    
if __name__ == "__main__":
    result = two_sum(nums = [2, 7, 11, 15],targer=9)
    print(result)