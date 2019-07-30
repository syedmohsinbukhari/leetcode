# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out_list = ListNode(0)
        out_run = out_list
        cf = 0
        while True:
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0
            sm = n1 + n2 + cf if n1 + n2 + cf < 10 else n1 + n2 + cf - 10
            cf = 1 if n1 + n2 + cf > 9 else 0

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            out_run.val = sm
            if (l1 is None) and (l2 is None) and (cf == 0):
                out_run.next = None
                break
            else:
                out_run.next = ListNode(0)
                out_run = out_run.next
        return out_list
