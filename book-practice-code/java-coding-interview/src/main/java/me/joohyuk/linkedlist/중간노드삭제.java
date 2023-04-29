package me.joohyuk.linkedlist;

public class 중간노드삭제 {

    public boolean deleteNode(LinkedListNode n) {
        if (n == null || n.next == null) {
            return false;   // 실패
        }
        LinkedListNode next = n.next;
        n.data = next.data;
        n.next = next.next;
        return true;
    }
}
