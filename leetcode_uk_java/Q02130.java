/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        ListNode tempNode = copyList(head);
        ListNode curr = copyList(head);
        ListNode rev = reverseNode(tempNode);
        int max = 0;
        while (curr != null && rev != null) {
            int temp = curr.val + rev.val;
            if (temp > max) {
                max = temp;
            }
            curr = curr.next;
            rev = rev.next;
        }
        return max;
    }

    public ListNode reverseNode(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public ListNode copyList(ListNode head) {
        if (head == null) return null;

        ListNode newHead = new ListNode(head.val);
        ListNode currOld = head.next;
        ListNode currNew = newHead;

        while (currOld != null) {
            currNew.next = new ListNode(currOld.val);
            currNew = currNew.next;
            currOld = currOld.next;
        }

        return newHead;
    }

}