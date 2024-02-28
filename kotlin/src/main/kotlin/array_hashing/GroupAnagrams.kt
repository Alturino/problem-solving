package org.example.array_hashing

fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val m = mutableMapOf<String, MutableList<String>>()

    for (str in strs) {
        val intArray = IntArray(26) { 0 }
        for (word in str) {
            intArray[word.code - 'a'.code] += 1
        }
        val key = intArray.joinToString()
        m[key] = m.getOrDefault(key, mutableListOf()).apply { add(str) }
    }
    return m.values.toList()
}

fun main() {
    println(groupAnagrams(arrayOf("eat", "tea", "tan", "ate", "nat", "bat")))
}