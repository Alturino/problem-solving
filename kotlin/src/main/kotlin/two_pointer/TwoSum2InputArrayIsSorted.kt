package org.example.two_pointer

fun twoSum(numbers: IntArray, target: Int): IntArray {
    var left = 0
    var right = numbers.size - 1

    while (left < right) {
        val sum = numbers[left] + numbers[right]
        if (sum == target) {
            return intArrayOf(left + 1, right + 1)
        }

        if (sum < target) {
            left++
        } else {
            right--
        }
    }
    return intArrayOf()
}

fun main() {
    val input = intArrayOf(2, 7, 11, 15)
    val target = 9
    val output = twoSum(input, target).toList()
    println("output: $output, expected: [1,2]")
}