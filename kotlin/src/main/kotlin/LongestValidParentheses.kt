package org.example

import java.util.Stack
import kotlin.math.max

// // Time O(N)
// // Space O(N)
fun longestValidParentheses(s: String): Int {
    val st = mutableListOf(-1)

    var res = 0
    for ((i, ch) in s.withIndex()) {
        if (ch == '(') {
            st.add(i)
       } else {
            st.removeLast()
            if (st.isEmpty()) {
                st.add(i)
            } else {
                res = max(res, i - st[st.lastIndex])
            }
        }
    }
    return res
}

// // Time O(N)
// // Space O(1)
//fun longestValidParentheses(s: String): Int {
//    var res = 0
//    var open = 0
//    var close = 0
//    for (ch in s) {
//        if (ch == '(') {
//            open++
//        } else {
//            close++
//        }
//
//        if (open == close) {
//            res = max(res, 2 * close)
//        } else if (open < close) {
//            open = 0
//            close = 0
//        }
//    }
//
//    open = 0
//    close = 0
//    for (ch in s.reversed()) {
//        if (ch == '(') {
//            open++
//        } else {
//            close++
//        }
//
//        if (open == close) {
//            res = max(res, 2 * close)
//        } else if (close < open) {
//            open = 0
//            close = 0
//        }
//    }
//
//    return res
//}

fun main() {
    var input = "(()"
    var output = longestValidParentheses(input)
    println("output: $output, expected: 2")

    input = ")()())"
    output = longestValidParentheses(input)
    println("output: $output, expected: 4")
}