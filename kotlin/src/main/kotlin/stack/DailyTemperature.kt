package org.example.stack

fun dailyTemperatures(temperatures: IntArray): IntArray {
    val st = mutableListOf<Pair<Int, Int>>() // index, temperature
    val res = IntArray(temperatures.size) { 0 }
    for ((i, temperature) in temperatures.withIndex()) {
        while (st.isNotEmpty() && temperature > st[st.lastIndex].second) {
            val (stIndex, _) = st.removeLast()
            res[stIndex] = i - stIndex
        }
        st.add(i to temperature)
    }
    return res
}