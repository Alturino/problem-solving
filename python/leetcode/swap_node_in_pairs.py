from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(val=0)
        prev, curr = dummy, head
        while curr and curr.next:
            temp = curr.next.next

            prev.next = curr.next
            curr.next.next = curr
            curr.next = temp

            prev = curr
            curr = temp
        return dummy.next


s = Solution()
print(
    s.swapPairs(
        ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4,
                        next=ListNode(val=5),
                    ),
                ),
            ),
        )
    )
)
