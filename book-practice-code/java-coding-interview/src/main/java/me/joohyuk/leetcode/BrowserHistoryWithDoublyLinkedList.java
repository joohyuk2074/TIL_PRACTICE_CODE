package me.joohyuk.leetcode;

public class BrowserHistoryWithDoublyLinkedList {

    private ListNode<String> head;
    private ListNode<String> current;

    public BrowserHistoryWithDoublyLinkedList(String homepage) {
        this.head = this.current = new ListNode<>(homepage, null, null);
    }

    public void visit(String url) {
        ListNode<String> newNode = new ListNode<>(url, null, null);
        this.current.next = newNode;
        newNode.prev = this.current;
        this.current = newNode;
    }

    public String back(int steps) {
        while (steps > 0 && this.current.prev != null) {
            steps -= 1;
            this.current = this.current.prev;
        }
        return this.current.value;
    }

    public String forward(int steps) {
        while (steps > 0 && this.current.next != null) {
            steps -= 1;
            this.current = this.current.next;
        }
        return this.current.value;
    }

    private static class ListNode<T> {
        private String value;

        private ListNode<T> next;

        private ListNode<T> prev;

        public ListNode(String value, ListNode<T> next, ListNode<T> prev) {
            this.value = value;
            this.next = next;
            this.prev = prev;
        }
    }

    public static void main(String[] args) {
        BrowserHistoryWithDoublyLinkedList browserHistoryWithDoublyLinkedList = new BrowserHistoryWithDoublyLinkedList("leetcode.com");
        browserHistoryWithDoublyLinkedList.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
        browserHistoryWithDoublyLinkedList.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
        browserHistoryWithDoublyLinkedList.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
        browserHistoryWithDoublyLinkedList.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
        browserHistoryWithDoublyLinkedList.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
        browserHistoryWithDoublyLinkedList.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
        browserHistoryWithDoublyLinkedList.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
        browserHistoryWithDoublyLinkedList.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
        browserHistoryWithDoublyLinkedList.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
        browserHistoryWithDoublyLinkedList.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
