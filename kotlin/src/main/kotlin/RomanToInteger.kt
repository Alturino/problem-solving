package org.example

fun romanToInt(s: String): Int {
    val m = mutableMapOf(
        'I' to 1,
        'V' to 5,
        'X' to 10,
        'L' to 50,
        'C' to 100,
        'D' to 500,
        'M' to 1000
    )

    var res = 0
    var currentMax = 0
    for (i in s.indices.reversed()) {
        if (m.containsKey(s[i])) {
            val currentKey = m[s[i]]!!
            if (currentKey >= currentMax) {
                currentMax = currentKey
                res += currentKey
            } else {
                res -= currentKey
            }
        }
    }

    return res
}

fun main() {
    var output = romanToInt("III")
    println("$output, ${output == 3}")
}