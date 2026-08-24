#Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            print("x: ", x, "y: ", y, "carry: ", carry)
            total = x + y + carry
            carry  = total // 10
            print("total: ", total, "carry: ", carry)

            current.next = ListNode(total % 10)
            print("current.next.val: ", current.next.val)
            current = current.next
            print("current.val: ", current.val)

            if l1:
                l1 = l1.next
                print("l1: ", l1.val if l1 else None)

            if l2:
                l2 = l2.next
                print("l2: ", l2.val if l2 else None)

        return dummy.next 
    

result = Solution().addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))),ListNode(5,ListNode(6,ListNode(4))))
print(result)
while result:
    print(result.val)
    result = result.next