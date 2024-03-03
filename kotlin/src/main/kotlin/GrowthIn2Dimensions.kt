package org.example

import kotlin.math.max

fun countMax(upRight: Array<String>): Long {
    val rc = upRight.map { it.split(" ") }.map { it[0].toInt() to it[1].toInt() }
    val gridLen = rc.map { max(it.first, it.second) }.maxBy { it }

    val grid = MutableList(gridLen) {
        MutableList(gridLen) {
            0
        }
    }

    var m = 0
    for ((row, col) in rc) {
        for (i in 0 until row) {
            for (j in 0 until col) {
                grid[i][j] += 1
                m = max(m, grid[i][j])
            }
        }
    }

    var count = 0
    for (i in 0 until gridLen) {
        for (j in 0 until gridLen) {
            if (grid[i][j] == m) {
                count++
            } else {
                continue
            }
        }
    }
    return count.toLong()
}

fun main() {
    var output = countMax(arrayOf("1 4", "2 3", "4 1"))
    println("output: $output, expected = 1")


    output = countMax(arrayOf("2 3", "3 7", "4 1"))
    println("output: $output, expected = 2")
}