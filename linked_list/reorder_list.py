from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"]) -> None:
        self.val = val
        self.next = next


class Solution:
    # # Time Complexity O(N)
    # # Space Complexity O(N)
    # # [1,2,3,4]
    # # [1,4,2,3]
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     curr = head
    #
    #     nodes = []
    #     while curr:
    #         nodes.append(curr.val)
    #         curr = curr.next
    #
    #     start, end = 0, len(nodes) - 1
    #     curr = head
    #     while start <= end and curr:
    #         curr.val = nodes[start]
    #
    #         if curr.next:
    #             curr = curr.next
    #             curr.val = nodes[end]
    #
    #         if curr.next:
    #             curr = curr.next
    #
    #         start += 1
    #         end -= 1

    # Time Complexity O(N)
    # Space Complexity O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second_half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge the first_half and second_half
        # Prev is the result of reversing the second half list
        reversed = prev
        first, second = head, reversed
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


s = Solution()
# s.reorderList(
#     head=ListNode(
#         val=1,
#         next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=None))),
#     )
# )
s.reorderList(
    head=ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5,
                        next=None,
                    ),
                ),
            ),
        ),
    )
)
