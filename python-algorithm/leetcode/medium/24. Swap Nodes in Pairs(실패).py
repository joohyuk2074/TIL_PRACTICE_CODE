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

        answer = []

        if head is None:
            return answer

        answer = pre = ListNode(0)
        pre.next = head

        while pre.next and pre.next.next:
            cur_node = pre.next
            next_node = cur_node.next

            pre.next = next_node
            cur_node.next = next_node.next
            next_node.next = cur_node
            pre = cur_node

        return answer.next


four = ListNode(4, None)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)
head = one
solution = Solution()
pairs = solution.swapPairs(head)
print(pairs)
