# 4. Remove Duplicates from Sorted Array
# Problem: Given a sorted array nums, remove the duplicates in-place such that each unique element appears only once. 
#         Return the number of unique elements (k). It doesn't matter what's left beyond the first k elements.
        
# Example:
# Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, and nums becomes [0, 1, 2, 3, 4, _, _, _, _, _](rest don't matter)

# Think about it: Since the array is sorted, all duplicate values are next to each other. 
#                 That's the key property that makes this solvable in-place with two pointers.
# Hint: Same slow/fast two-pointer idea as Move Zeroes!

# slow = position of the last unique element placed so far
# fast = scans ahead looking for a new value that's different from nums[slow]

# When nums[fast] != nums[slow], it means you've found a new unique value — move it next to the last unique one.


def remove_duplicate(nums):
    unique_val = set()
    unique_count = 0
    for num in nums:
        if num not in unique_val:
            unique_val.add(num)
            unique_count += 1
    return unique_count


def remove_duplicate_1(nums):
    prev = nums[0]
    slow = 1
    for curr in range(len(nums)):
        if nums[curr] != nums[prev]:
            nums[prev] = nums[curr]
            slow+=1
    return slow


def remove_duplicate_2(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

        
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = remove_duplicate(nums)
    print(result)
    # result_1 = remove_duplicate_1(nums)
    # print(result_1)
    result_2 = remove_duplicate_2(nums)
    print(result_2)