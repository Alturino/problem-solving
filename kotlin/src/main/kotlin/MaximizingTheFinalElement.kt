package org.example

import kotlin.math.abs
import kotlin.math.max


fun getMaxValue(arr: Array<Int>): Int {
    arr.sort()
    var res = arr[0]
    for (i in 0 until arr.size - 1) {
        var diff = abs(arr[i] - arr[i + 1])
        while (diff > 1) {
            arr[i + 1] -= diff - 1
            diff = 0
        }
        res = max(res, arr[i])
    }
    return max(res, arr[arr.lastIndex])
}

fun main() {
    var input = arrayOf(3, 1, 3, 4)
    var output = getMaxValue(input)
    println("output: $output, expected: 4")

    input = arrayOf(1, 3, 2, 2)
    output = getMaxValue(input)
    println("output: $output, expected: 3")


    input = arrayOf(3, 2, 3, 5)
    output = getMaxValue(input)
    println("output: $output, expected: 4")
}