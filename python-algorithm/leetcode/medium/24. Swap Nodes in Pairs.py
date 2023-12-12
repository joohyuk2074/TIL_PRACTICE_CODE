# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        cur_node = head
        next_node = cur_node.next
        head = next_node

        while next_node is not None:
            cur_node.next = next_node.next
            next_node.next = cur_node

            cur_node = cur_node.next
            if cur_node is None:
                break

            next_node = cur_node.next

        return head
