package org.example

//data class TrieNode(
//    val children: MutableMap<Char, TrieNode> = mutableMapOf(),
//    var isEnd: Boolean = false
//)
//
//data class Trie(val root: TrieNode = TrieNode()) {
//    fun insert(s: String) {
//        var curr = root
//        for (ch in s) {
//            curr.children[ch] = curr.children.getOrDefault(ch, TrieNode())
//            curr = curr.children[ch]!!
//        }
//        curr.isEnd = true
//    }
//
//    fun check(s: String): String {
//        var curr = root
//        val sb = StringBuilder()
//        for (ch in s) {
//            if (!curr.children.containsKey(ch)) {
//                return s
//            }
//            curr = curr.children[ch]!!
//            sb.append(ch)
//            if (curr.isEnd) {
//                return sb.toString()
//            }
//        }
//        return s
//    }
//
//}
//
//fun replaceWords(dictionary: List<String>, sentence: String): String {
//    val trie = Trie()
//    val map = dictionary.associateWith {
//        trie.insert(it)
//        it
//    }
//
//    val words = sentence.split(" ").toMutableList()
//
//    for ((i, word) in words.withIndex()) {
//        val inTrie = trie.check(word)
//        if (map.containsKey(inTrie)) {
//            words[i] = map[inTrie]!!
//        }
//    }
//    return words.joinToString(" ")
//}


fun replaceWords(dictionary: List<String>, sentence: String): String {
    val s = dictionary.toSet()

    val sb = StringBuilder()
    for (word in sentence.split(" ")) {
        var prefix = ""
        for (i in 1..word.length) {
            prefix = word.substring(0, i)
            if (s.contains(prefix)) {
                break
            }
        }
        if (sb.isNotEmpty()) {
            sb.append(" ")
        }
        sb.append(prefix)
    }
    return sb.toString()
}

fun main() {
    val output = replaceWords(listOf("cat", "bat", "rat"), sentence = "the cattle was rattled by the battery")
    println(output)
}