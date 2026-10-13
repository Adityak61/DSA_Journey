/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        Node curr = head;
        while(curr!=null){
            if(curr.child!=null){
                Node child=curr.child;
                Node next=curr.next;
                curr.next=child;
                child.prev=curr;
                Node temp=child;
                while(temp.next!=null){
                    temp=temp.next;
                }
                temp.next=next;
                if(temp.next!=null){
                    next.prev=temp;
                }
                curr.child=null;
            }
            curr=curr.next;
        }
        return head;
    }
}