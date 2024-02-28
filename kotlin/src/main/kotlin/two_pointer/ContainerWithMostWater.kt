package org.example.two_pointer

import kotlin.math.max
import kotlin.math.min

fun maxArea(height: IntArray): Int {
    var left = 0
    var right = height.size - 1

    var res = 0
    while (left <= right) {
        val maxArea = min(height[left], height[right]) * (right - left)
        res = max(res, maxArea)

        if (height[left] < height[right]) {
            left++
        } else {
            right--
        }
    }

    return res
}

fun main() {
    val input = intArrayOf(1, 8, 6, 2, 5, 4, 8, 3, 7)
    val output = maxArea(input)
    println("output: $output, expected: 49")
}
