package org.example.neetcode_roadmap.array_hashing

fun topKFrequent(nums: IntArray, k: Int): IntArray {
    val valueToCount = mutableMapOf<Int, Int>() // value -> count
    for (num in nums) {
        valueToCount[num] = valueToCount.getOrDefault(num, 0) + 1
    }

    val res = mutableListOf<Int>()
    val countToValues = MutableList(nums.size + 1) {
        mutableListOf<Int>()
    }
    for ((value, count) in valueToCount) {
        countToValues[count].add(value)
    }

    for (i in countToValues.indices.reversed()) {
        for (value in countToValues[i]) {
            if (res.size == k) {
                return res.toIntArray()
            }
            res.add(value)
        }
    }

    return res.toIntArray()
}

fun main() {
    println(topKFrequent(nums = intArrayOf(1, 1, 1, 2, 2, 3), k = 2).toList())
    println(topKFrequent(nums = intArrayOf(1), k = 1).toList())
}