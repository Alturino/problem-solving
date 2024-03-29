package org.example.neetcode_roadmap.stack

import kotlin.math.max

fun largestRectangleArea(heights: IntArray): Int {
    var res = 0
    val st = mutableListOf<Pair<Int, Int>>() // index, height
    for ((i, height) in heights.withIndex()) {
        var start = i
        while (st.isNotEmpty() && st[st.lastIndex].second > height) {
            val (stIndex, stHeight) = st.removeLast()
            res = max(res, stHeight * (i - stIndex))
            start = stIndex
        }
        st.add(start to height)
    }

    for ((i, height) in st) {
        res = max(res, height * (heights.size - i))
    }

    return res
}