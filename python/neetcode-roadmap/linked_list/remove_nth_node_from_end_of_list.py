from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"]) -> None:
        self.val = val
        self.next = next


class Solution:
    ## Time Complexity O(2N)
    ## Space Complexity O(1)
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     def reverseNode(head: Optional[ListNode]) -> Optional[ListNode]:
    #         prev, curr = None, head
    #         while curr:
    #             temp = curr.next
    #             curr.next = prev
    #             prev = curr
    #             curr = temp
    #         return prev
    #
    #     reversed = reverseNode(head)
    #     res = dummy = ListNode(0, reversed)
    #
    #     count = 1
    #     while reversed:
    #         if count == n:
    #             dummy.next = reversed.next
    #         else:
    #             dummy = reversed
    #
    #         reversed = reversed.next
    #         count += 1
    #
    #     res = reverseNode(res.next)
    #     return res

    # Time Complexity O(N)
    # Space Complexity O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


s = Solution()
s.removeNthFromEnd(
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
    ),
    n=2,
)
