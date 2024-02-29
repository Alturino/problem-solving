package org.example.stack

import java.util.Stack

fun evalRPN(tokens: Array<String>): Int {
    val validOperators = setOf("+", "-", "*", "/")
    val st = Stack<Int>()
    for (token in tokens) {
        if (!validOperators.contains(token)) {
            st.push(token.toInt())
            continue
        }
        if (validOperators.contains(token)) {
            val second = st.pop()
            val first = st.pop()
            when (token) {
                "+" -> {
                    st.push(first + second)
                }

                "*" -> {
                    st.push(first * second)
                }

                "-" -> {
                    st.push(first - second)
                }

                "/" -> {
                    st.push(first / second)
                }
            }
        }
    }
    return st.pop()
}

fun main() {
    val input = arrayOf("4", "13", "5", "/", "+")
    val output = evalRPN(tokens = input)
    println("output: $output, expected: 6")
}