package neetcode_roadmap.backtracking

fun exist(board: Array<CharArray>, word: String): Boolean {
    val visited = mutableSetOf<Pair<Int, Int>>()

    fun dfs(row: Int, col: Int, i: Int): Boolean {
        if (i == word.length) {
            return true
        }

        if (!board.indices.contains(row) || !board[row].indices.contains(col) || visited.contains(row to col) || board[row][col] != word[i]) {
            return false
        }

        visited.add(row to col)
        val res =
            dfs(row + 1, col, i + 1) || dfs(row - 1, col, i + 1) || dfs(row, col + 1, i + 1) || dfs(row, col - 1, i + 1)
        visited.remove(row to col)
        return res
    }

    for (row in board.indices) {
        for (col in board[row].indices) {
            if (dfs(row, col, 0)) {
                return true
            }
        }
    }
    return false
}

fun main() {
    val output = exist(
        board = arrayOf(
            charArrayOf('A', 'B', 'C', 'E'),
            charArrayOf('S', 'F', 'C', 'S'),
            charArrayOf('A', 'D', 'E', 'E')
        ),
        word = "ABCCED"
    )
    println(output)
}