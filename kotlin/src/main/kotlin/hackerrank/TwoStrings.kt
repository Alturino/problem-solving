package org.example.hackerrank

fun twoStrings(s1: String, s2: String): String {
    val set1 = MutableList(26) {
        false
    }
    for (ch in s1) {
        set1[ch.code - 'a'.code] = true
    }

    val set2 = MutableList(26) {
        false
    }
    for (ch in s2) {
        set2[ch.code - 'a'.code] = true
    }

    for (i in set1.indices) {
        if (!set1[i] || !set2[i]) {
            continue
        }

        if (set1[i] == set2[i]) {
            return "YES"
        }
    }
    return "NO"
}

fun main() {
    println(twoStrings("and", "art"))
    println(twoStrings("hi", "world"))
}