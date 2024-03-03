package org.example

fun getSmallestString(n: Int, k: Int): String {
    val res = MutableList(n) { 0 }
    var remaining = k - res.size

    var index = res.lastIndex
    while (remaining > 25) {
        res[index] = 25
        remaining -= 25
        index--
    }
    res[index] = remaining

    return res.joinToString("") { (it + 'a'.code).toChar().toString() }
}

fun main() {
    var output = getSmallestString(3, 27)
    println("output: $output, expected: aay")
}