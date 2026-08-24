# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def longestPalindrome(string):
    def helper(left,right):
        while left >=0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left+1:right]
    longest = ""
    for i in range(len(string)):
        
        odd = helper(i, i)
        even = helper(i, i + 1)
        print(odd)
        print(even)
        if len(odd) > len(longest):
            longest = odd

        if len(even) > len(longest):
            longest = even
    return longest
res = longestPalindrome("babad")
print("********res",res)
