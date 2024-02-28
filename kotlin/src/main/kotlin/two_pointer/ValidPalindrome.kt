package org.example.two_pointer

fun isPalindrome(s: String): Boolean {
    var left = 0
    var right = s.length - 1
    val lowered = s.lowercase()
    while (left <= right) {
        if (!lowered[left].isLetterOrDigit()) {
            left++
            continue
        }
        if (!lowered[right].isLetterOrDigit()) {
            right--
            continue
        }
        if (lowered[left] != lowered[right]) {
            return false
        }
        left++
        right--
    }
    return true
}

fun main() {
    val input = "A man, a plan, a canal: Panama"
    val output = isPalindrome(input)
    println("input: $input, output: $output, expected: true")
}