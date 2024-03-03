package org.example.neetcode_roadmap.backtracking

fun partition(s: String): List<List<String>> {
    fun isPalindrome(left: Int, right: Int): Boolean {
        var left = left
        var right = right
        while (left <= right) {
            if (s[left] != s[right]) {
                return false
            }
            left++
            right--
        }
        return true
    }

    val res = mutableListOf<List<String>>()
    val partition = mutableListOf<String>()
    fun backtracking(start: Int = 0) {
        if (start >= s.length) {
            res.add(partition.toList())
            return
        }

        for (i in start until s.length) {
            if (isPalindrome(start, i)) {
                partition.add(s.substring(start..i))
                backtracking(i + 1)
                partition.removeLast()
            }
        }
    }
    backtracking()
    return res
}

fun main() {
    var input = "aab"
    var output = partition(input)
    println("output: $output, expected: [[a,a,b],[aa,b]]")
}