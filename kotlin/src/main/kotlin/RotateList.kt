package org.example


data class ListNode(val `val`: Int = 0, var next: ListNode? = null)

fun rotateRight(head: ListNode?, k: Int): ListNode? {
    val q = ArrayDeque<ListNode>()

    var curr = head
    while (curr != null) {
        q.addLast(curr)
        curr = curr.next
    }

    var prev = head
    for (i in 0 until k) {
        val node = q.removeLast()
        if (prev != null) {
            node.next = prev
            prev = prev.next
        }
        q.addFirst(node)
    }

    val res = ListNode()
    curr = res
    while (q.isNotEmpty()) {
        curr?.next = q.removeFirst()
        curr = curr?.next
    }
    return res.next
}

fun main() {
    val input = ListNode(
        `val` = 1,
        next = ListNode(
            `val` = 2,
            next = ListNode(
                `val` = 3,
                next = ListNode(
                    `val` = 4,
                    next = ListNode(`val` = 5)
                )
            ),
        )
    )
    rotateRight(input, k = 2)
}