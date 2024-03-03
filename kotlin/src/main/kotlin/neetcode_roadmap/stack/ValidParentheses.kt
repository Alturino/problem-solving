package org.example.neetcode_roadmap.stack

import java.util.Stack

fun isValid(s: String): Boolean {
    val braces = mutableMapOf(')' to '(', ']' to '[', '}' to '{')
    val st = Stack<Char>()

    for (ch in s) {
        if (braces.containsKey(ch) && st.isEmpty()) {
            return false
        }
        if (braces.containsKey(ch) && st.peek() == braces[ch]) {
            st.pop()
        } else {
            st.add(ch)
        }
    }

    return st.isEmpty()
}

fun main() {
    var input = "()"
    var output = isValid(input)
    println("output: $output, expected: true")


    input = "()[]{}"
    output = isValid(input)
    println("output: $output, expected: true")

    input = "(]"
    output = isValid(input)
    println("output: $output, expected: false")
}