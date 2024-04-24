from typing import Optional


class Node:
    def __init__(
        self,
        x: int,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    #     curr = head
    #     oldToCopy = {None: None}
    #     while curr:
    #         copy = Node(curr.val)
    #         oldToCopy[curr] = copy
    #         curr = curr.next
    #
    #     curr = head
    #     while curr:
    #         copy = oldToCopy[curr]
    #         copy.next = oldToCopy[curr.next]
    #         copy.random = oldToCopy[curr.random]
    #         curr = curr.next
    #
    #     return oldToCopy[head]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        curr = head
        while curr:
            next = curr.next
            curr.next = Node(curr.val)
            curr.next.next = next
            curr = next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        copy = copyCurr = head.next
        while copyCurr.next:
            curr.next = curr.next.next

            copyCurr.next = copyCurr.next.next
            copyCurr = copyCurr.next

        curr.next = curr.next.next

        return copy
