class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def reverse_linked_list(node: Node) -> Node:
    if not node or not node.next:
        return node
    end = reverse_linked_list(node.next)
    node.next.next = node
    node.next = None
    return end


before = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
reversed = reverse_linked_list(Node(1, Node(2, Node(3, Node(4, Node(5, None))))))

while before:
    print("Before ", before.val)
    before = before.next

while reversed:
    print("Reversed ", reversed.val)
    reversed = reversed.next
