package org.example.neetcode_roadmap.stack

import java.util.Stack

fun carFleet(target: Int, position: IntArray, speed: IntArray): Int {
    val cars = position.zip(speed).sortedByDescending { it.first }
    val st = Stack<Float>()
    for ((p, s) in cars) {
        st.push((target - p).toFloat() / s)
        if (st.size >= 2 && st[st.lastIndex] <= st[st.lastIndex - 1]) {
            st.pop()
        }
    }
    return st.size
}

fun main() {
    val output = carFleet(target = 10, position = intArrayOf(6, 8), speed = intArrayOf(3, 2))
    println("output: $output, result: ${output == 2}")
}