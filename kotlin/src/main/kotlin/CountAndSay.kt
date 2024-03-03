package org.example

fun coundAndSay(n: Int): String {
    if (n == 1) {
        return "1"
    }

    if (n == 2) {
        return "11"
    }

    val ssb = StringBuilder()
    ssb.append("11")
    for (i in 3..n) {
        val sb = StringBuilder()
        task(ssb.toString(), sb)
        ssb.setLength(0)
        ssb.append(sb)
    }
    return ssb.toString()
}

private fun task(s: String, sb: StringBuilder) {
    var count = 1
    for (i in 0 until s.length - 1) {
        if (s[i] == s[i + 1]) {
            count++
        } else {
            sb.append(count)
            sb.append(s[i])
            count = 1
        }
    }
    sb.append(count)
    sb.append(s[s.lastIndex])
}

fun main() {
    var input = 1
    var output = coundAndSay(n = input)
    println("output: $output, expected: 1")

    input = 4
    output = coundAndSay(n = input)
    println("output: $output, expected: 1211")
}