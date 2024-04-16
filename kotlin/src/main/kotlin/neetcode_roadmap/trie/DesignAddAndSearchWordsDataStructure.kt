package org.example.neetcode_roadmap.trie

data class TrieNode(
    val children: MutableMap<Char, TrieNode> = mutableMapOf(),
    var isWord: Boolean = false
)

data class WordDictionary(private val root: TrieNode = TrieNode()) {

    fun addWord(word: String) {
        var curr = root
        for (ch in word) {
            if (!curr.children.containsKey(ch)) {
                curr.children[ch] = TrieNode()
            }
            curr = curr.children[ch]!!
        }
        curr.isWord = true
    }

    fun search(word: String): Boolean {
        fun dfs(j: Int, node: TrieNode): Boolean {
            var curr = node
            for (i in j until word.length) {
                val char = word[i]
                if (char == '.') {
                    for (child in curr.children.values) {
                        return dfs(i + 1, child)
                    }
                    return false
                } else {
                    if (!curr.children.containsKey(char)) {
                        return false
                    }
                    curr = curr.children[char]!!
                }
            }
            return curr.isWord
        }
        return dfs(0, root)
    }

}

fun main() {
    val wd = WordDictionary()
    println(wd.addWord("a"))
    println(wd.addWord("a"))
    println(wd.search("."))
    println(wd.search("a"))
    println(wd.search("aa"))
    println(wd.search("a"))
    println(wd.search(".a"))
    println(wd.search("a."))
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = WordDictionary()
 * obj.addWord(word)
 * ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
 * [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
 * var param_2 = obj.search(word)
 */