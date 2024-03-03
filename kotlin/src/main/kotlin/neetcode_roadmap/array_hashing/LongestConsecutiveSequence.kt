package org.example.neetcode_roadmap.array_hashing

import kotlin.math.max


fun longestConsecutive(nums: IntArray): Int {
    val set = nums.toSet()
    var res = 0
    for (num in set) {
        if (!set.contains(num - 1)) {
            var length = 1
            while (set.contains(num + length)) {
                length += 1
            }
            res = max(res, length)
        }
    }
    return res
}

fun main() {
    println(longestConsecutive(nums = intArrayOf(100, 4, 200, 1, 3, 2)))
}