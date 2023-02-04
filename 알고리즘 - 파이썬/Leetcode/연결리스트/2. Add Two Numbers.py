# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret_list = ListNode(0)
        dummy_list = ret_list

        carry = 0
        while l1 != None or l2 != None or carry == 1:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            sum_val = l1_val + l2_val + carry
            carry = sum_val // 10
            next_node = ListNode(sum_val % 10)
            ret_list.next = next_node
            ret_list = ret_list.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            

        return dummy_list.next