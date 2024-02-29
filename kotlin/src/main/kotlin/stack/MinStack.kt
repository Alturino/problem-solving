package org.example.stack

import java.util.Stack
import kotlin.math.min

class MinStack {
    private val st = Stack<Int>()
    private val minst = Stack<Int>()

    fun push(`val`: Int) {
        if (minst.isNotEmpty() && minst.peek() < `val`) {
            val temp = minst.peek()
            minst.push(temp)
            st.push(`val`)
        } else {
            minst.push(`val`)
            st.push(`val`)
        }
    }

    fun pop() {
        st.pop()
        minst.pop()
    }

    fun top(): Int {
        return st.peek()
    }

    fun getMin(): Int {
        return minst.peek()
    }
}