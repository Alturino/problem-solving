package org.example.stack

fun generateParenthesis(n: Int): List<String> {
    val res = mutableListOf<String>()
    val combination = mutableListOf<Char>()
    fun backtracking(open: Int = 0, close: Int = 0) {
        if (open == n && close == n) {
            res.add(combination.joinToString(""))
            return
        }

        if (open < n) {
            combination.add('(')
            backtracking(open + 1, close)
            combination.removeLast()
        }

        if (close < open) {
            combination.add(')')
            backtracking(open, close + 1)
            combination.removeLast()
        }
    }
    backtracking()
    return res
}

fun main() {
    var input = 3
    var output = generateParenthesis(input)
    println("output: $output, expected: [((())),(()()),(())(),()(()),()()()]")

    input = 1
    output = generateParenthesis(input)
    println("output: $output, expected: [()]")
}