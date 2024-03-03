package org.example.neetcode_roadmap.array_hashing

fun isValidSudoku(board: Array<CharArray>): Boolean {
    val rs = mutableMapOf<Int, MutableSet<Char>>()
    val cs = mutableMapOf<Int, MutableSet<Char>>()
    val bs = mutableMapOf<Pair<Int, Int>, MutableSet<Char>>()

    for (row in board.indices) {
        for (col in board[row].indices) {
            if (board[row][col] == '.') {
                continue
            }
            if (rs[row]?.contains(board[row][col]) == true || cs[col]?.contains(board[row][col]) == true || bs[row / 3 to col / 3]?.contains(
                    board[row][col]
                ) == true
            ) {
                return false
            }
            rs[row] = rs.getOrDefault(row, mutableSetOf()).apply { add(board[row][col]) }
            cs[col] = cs.getOrDefault(col, mutableSetOf()).apply { add(board[row][col]) }
            bs[row / 3 to col / 3] = bs.getOrDefault(row / 3 to col / 3, mutableSetOf()).apply { add(board[row][col]) }
        }
    }
    return true
}

fun main() {
    var board = arrayOf(
        charArrayOf('8', '3', '.', '.', '7', '.', '.', '.', '.'),
        charArrayOf('6', '.', '.', '1', '9', '5', '.', '.', '.'),
        charArrayOf('.', '9', '8', '.', '.', '.', '.', '6', '.'),
        charArrayOf('8', '.', '.', '.', '6', '.', '.', '.', '3'),
        charArrayOf('4', '.', '.', '8', '.', '3', '.', '.', '1'),
        charArrayOf('7', '.', '.', '.', '2', '.', '.', '.', '6'),
        charArrayOf('.', '6', '.', '.', '.', '.', '2', '8', '.'),
        charArrayOf('.', '.', '.', '4', '1', '9', '.', '.', '5'),
        charArrayOf('.', '.', '.', '.', '8', '.', '.', '7', '9'),
    )
    var output = isValidSudoku(board = board)
    println("output: $output, expected: false")
}
