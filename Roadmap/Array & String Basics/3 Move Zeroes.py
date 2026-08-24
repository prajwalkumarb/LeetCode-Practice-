# Move Zeroes
# Problem: Given an array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. 
#           You must do this in-place (don't create a new array) and without making an extra copy.
# Example:
# Input:  nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# Think about it: you want all the non-zero elements to slide to the front (keeping their order) and all the zeroes to end up at the back.
# Hint: Try the two-pointer idea — one pointer (i) scans through the array, 
#   and another pointer (insert_pos or similar) tracks where the next non-zero element should go. 
#   Whenever you find a non-zero value while scanning, place it at insert_pos and increment insert_pos. 
#   At the end, fill whatever's left with zeroes.

# O(n) method
def move_zeros(nums):
    insert_pos = []
    insert_zero = []
    for i in nums:
        if i != 0:
            insert_pos.append(i)
        else:
            insert_zero.append(i)
    insert_pos.extend(insert_zero)
    return insert_pos


# O(1) method
# image ref 
# P:\Python_lib\Roadmap\Array & String Basics\Move-Zeros.png
def moveZero(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow+=1
    return nums

if __name__ == "__main__":
    restult = move_zeros(nums = [0, 1, 0, 3, 12])
    print(restult)
    
    print(moveZero([0, 1, 0, 3, 12]))
    