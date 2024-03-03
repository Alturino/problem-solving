package org.example.neetcode_roadmap.backtracking

fun subsets(nums: IntArray): List<List<Int>> {
    val res = mutableListOf<List<Int>>()
    val subset = mutableListOf<Int>()

    fun backtracking(i: Int = 0) {
        if (i >= nums.size) {
            res.add(subset.toList())
            return
        }
        subset.add(nums[i])
        backtracking(i + 1)
        subset.removeLast()
        backtracking(i + 1)
    }
    backtracking()
    return res
}

fun main() {
    val output = subsets(nums = intArrayOf(1, 2, 3))
    println(output)
}