# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getNode(self, head, index):
        cur_node = head
        while index != 0:
            cur_node = cur_node.next
            index -= 1
        return cur_node

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 전체 node수 구하기
        start_node = head
        node_length = 0
        while start_node is not None:
            node_length += 1
            start_node = start_node.next

        cur_idx = node_length - n - 1
        if cur_idx < 0:
            return head.next
        else:
            cur_node = self.getNode(head, cur_idx)
            cur_node.next = cur_node.next.next

        return head


node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1

solution = Solution()
end = solution.removeNthFromEnd(head, 2)
print(end)
