package org.example.neetcode_roadmap.two_pointer

fun threeSum(nums: IntArray): List<List<Int>> {
    nums.sort()
    val res = mutableListOf<List<Int>>()
    for ((i, num) in nums.withIndex()) {
        if (num > 0) {
            break
        }
        if (i > 0 && num == nums[i - 1]) {
            continue
        }
        var left = i + 1
        var right = nums.size - 1
        while (left < right) {
            val sum = num + nums[left] + nums[right]
            if (sum < 0) {
                left++
            } else if (sum > 0) {
                right--
            } else {
                res.add(listOf(num, nums[left], nums[right]))
                left++
                right--
                while (nums[left] == nums[left - 1] && left < right) {
                    left++
                }
            }
        }
    }
    return res
}