from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        prevGroup = dummyNode

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next

            prev, curr = kth.next, prevGroup.next
            while curr != nextGroup:
                tempNext = curr.next
                curr.next = prev
                prev = curr
                curr = tempNext

            tempGroup = prevGroup.next
            prevGroup.next = kth
            prevGroup = tempGroup

        return dummyNode.next

    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
