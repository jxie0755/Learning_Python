# LC328 Odd Even Linked List
# Medium


# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place.
# The program should run in O(1) space complexity and O(nodes) time complexity.


# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

from a0_ListNode import *


class Solution:

    # Veriosn A
    # Move Nodes out and combine back, O(1) but not in-Place
    def oddEvenList(self, head: ListNode) -> ListNode:
        O = odd = ListNode("O")
        E = even = ListNode("E")

        idx = 1
        while head:
            next_head = head.next
            head.next = None
            if idx % 2 != 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = next_head
            idx += 1

        # Merge Odd and Even
        odd.next = E.next
        return O.next

    # Veriosn B
    # Move Nodes out and combine back, O(1) and in-Place
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head or not head.next or not head.next.next:
            return head

        cur = head
        next_odd = cur.next.next
        even_tail = cur.next  # 注意这个even_tail一开始就是even_head,但是不能写在一起,因为随后会分开

        while next_odd:
            even_head = cur.next  # even_head维持不变,永远是第一个偶数节点
            real_tail = next_odd.next

            cur.next = next_odd
            next_odd.next = even_head
            even_tail.next = real_tail
            even_tail = real_tail

            cur = cur.next
            if real_tail:
                next_odd = real_tail.next
            else:
                break

        return head


if __name__ == "__main__":
    assert repr(Solution().oddEvenList(None)) == "None", "Edge 0"

    assert repr(Solution().oddEvenList(genNode([1, 2, 3, 4, 5]))) == "1->3->5->2->4", "Example 1"
    assert repr(Solution().oddEvenList(genNode([1, 2, 3, 4, 5, 6]))) == "1->3->5->2->4->6", "Example 1b"
    assert repr(Solution().oddEvenList(genNode([2, 1, 3, 5, 6, 4, 7]))) == "2->3->6->7->1->5->4", "Example 2"

    print("All passed")
