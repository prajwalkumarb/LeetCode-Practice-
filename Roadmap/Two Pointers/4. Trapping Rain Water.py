# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Input: height = [4,2,0,3,2,5]
# Output: 9

# refer image : P:\Python_lib\LeetCode-Practice-\Roadmap\Two Pointers\Q4.rainwatertrap.png


# Solution 1: Max Left, Max Right

def trap_1(height):
    n = len(height)
    maxleft = [0] * n
    maxright = [0] * n
    
    maxleft[0] = height[0]
    for i in range(1,n):
        maxleft[i] = max(maxleft[i-1],height[i])

    maxright[n-1] = height[n-1]
    for i in range(n-2,-1,-1):
        maxright[i] = max(maxright[i+1],height[i])
        
    water=0
    for i in range(n):
        water += min(maxleft[i],maxright[i]) - height[i]
        
    return water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap_1(height))
