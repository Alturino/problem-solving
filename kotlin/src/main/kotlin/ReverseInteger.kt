package org.example

import kotlin.Int.Companion.MAX_VALUE
import kotlin.Int.Companion.MIN_VALUE

fun reverse(x: Int): Int {
    var n = x
    var reversed = 0
    while (n != 0) {
        val lastDigit = n % 10
        if (reversed > MAX_VALUE / 10 || (reversed == MAX_VALUE / 10 && lastDigit >= MAX_VALUE % 10)) {
            return 0
        }
        if (reversed < MIN_VALUE / 10 || (reversed == MIN_VALUE / 10 && lastDigit <= MIN_VALUE % 10)) {
            return 0
        }
        reversed = reversed * 10 + lastDigit
        n /= 10
    }
    return reversed
}

fun main() {
    val output = reverse(-123)
    println(output)
    println("Int.MAX_VALUE: $MAX_VALUE, Int.MAX_VALUE: $MIN_VALUE")
}