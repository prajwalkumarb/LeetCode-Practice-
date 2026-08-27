# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def valid_palindrome(string):
    execuld_char =[" ",",",":"]
    for char in execuld_char:
        string = string.replace(char,"")
    lower_string = string.lower()
    string_1 = lower_string[::-1]
    if lower_string == string_1:
        return True
    else:
        return False

def valid_palindrome_1(string):
    left = 0
    right = len(string) - 1
    while left < right:
        while not string[left].isalnum():
            left += 1
        while not string[right].isalnum():
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1
    return True
    
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    value  = valid_palindrome(s)
    print(value)
    value_1 = valid_palindrome_1(s)
    print(value_1)