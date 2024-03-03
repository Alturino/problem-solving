package org.example.neetcode_roadmap.two_pointer

import kotlin.math.max

fun trap(height: IntArray): Int {
    var left = 0
    var maxLeft = height[left]

    var right = height.size - 1
    var maxRight = height[right]

    var sum = 0
    while (left < right) {
        if (maxLeft < maxRight) {
            left++
            maxLeft = max(maxLeft, height[left])
            sum += maxLeft - height[left]
        } else {
            right--
            maxRight = max(maxRight, height[right])
            sum += maxRight - height[right]
        }
    }
    return sum
}

fun main() {
    val input = intArrayOf(0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)
    val output = trap(input)
    println("output: $output, expected: 6")
}