package org.example.advent_of_code

import java.io.File

fun day1Part1(lines: List<String>): Int {
    var res = 0
    for (line in lines) {
        var left = 0
        var right = line.lastIndex
        while (left <= right) {
            if (!line[left].isDigit()) {
                left++
            }
            if (!line[right].isDigit()) {
                right--
            }

            if (line[left].isDigit() && line[right].isDigit()) {
                res += "${line[left]}${line[right]}".toInt()
                break
            }
        }
    }
    return res
}

// // Try to using Trie but didn't work I gave up
//data class TrieNode(val children: MutableMap<Char, TrieNode> = mutableMapOf(), var isWord: Boolean = false) {
//    fun insert(word: String) {
//        var curr = this
//        for (ch in word) {
//            if (!curr.children.containsKey(ch)) {
//                curr.children[ch] = TrieNode()
//            }
//            curr = curr.children[ch]!!
//        }
//    }
//
//    fun startWith(word: String): Boolean {
//        var curr = this
//        for (ch in word) {
//            if (!curr.children.containsKey(ch)) {
//                return false
//            }
//            curr = curr.children[ch]!!
//        }
//        return true
//    }
//}
//
//fun day1Part2(lines: List<String>): Int {
//    val wordToDigit = mapOf(
//        "one" to 1,
//        "two" to 2,
//        "three" to 3,
//        "four" to 4,
//        "five" to 5,
//        "six" to 6,
//        "seven" to 7,
//        "eight" to 8,
//        "nine" to 9
//    )
//    val trie = TrieNode().apply {
//        wordToDigit.keys.forEach { insert(it) }
//    }
//    var res = 0
//    for (line in lines) {
//        var left = 0
//        var right = 1
//        val nums = mutableListOf<Int>()
//        while (right in 1 until line.length) {
//            if (line[left].isDigit()) {
//                nums.add(line[left].digitToInt())
//                break
//            }
//
//            var window = line.substring(left..right)
//            while (left < line.length && left < right && !trie.startWith(window)) {
//                left++
//                window = line.substring(left..right)
//            }
//            if (wordToDigit.containsKey(window)) {
//                nums.add(wordToDigit[window]!!)
//                break
//            }
//            right++
//        }
//
//        left = line.length - 2
//        right = line.length - 1
//        while (left in line.length - 2 downTo 0) {
//            if (line[right].isDigit()) {
//                nums.add(line[right].digitToInt())
//                break
//            }
//
//            var window = line.substring(left..right)
//            while (left > 0 && !trie.startWith(window)) {
//                left--
//                window = line.substring(left..right)
//            }
//            if (wordToDigit.containsKey(window)) {
//                nums.add(wordToDigit[window]!!)
//                break
//            }
//            right--
//        }
//
//        res += nums.joinToString("").toInt()
//    }
//
//    return res
//}

//fun day1Part2(lines: List<String>): Int{
//    return lines.sumOf {
//        it.firstNotNullOfOrNull {  }
//    }
//}

fun main() {
//    val input = listOf("1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet")
//    val output = day1Part1(input)
//    println(output)


//    val input = listOf(
//        "two1nine",
//        "eightwothree",
//        "abcone2threexyz",
//        "xtwone3four",
//        "4nineeightseven2",
//        "zoneight234",
//        "7pqrstsixteen"
//    )
//    val output = day1Part2(input)
//    println(output)

    val input = File("./src/main/kotlin/advent_of_code/day1.in").readLines()
    val output = day1Part1(input)
    println(output)
}