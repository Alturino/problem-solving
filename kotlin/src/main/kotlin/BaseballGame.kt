package org.example

fun calPoints(operations: Array<String>): Int {
    val st = mutableListOf<Int>()

    for (operation in operations) {
        if (operation == "C") {
            st.removeLast()
        } else if (operation == "D") {
            val num = st[st.lastIndex]
            val res = num * 2
            st.add(res)
        } else if (operation == "+") {
            val first = st.removeLast()
            val second = st[st.lastIndex]
            st.add(first)
            st.add(first + second)
        } else {
            st.add(operation.toInt())
        }
    }

    var res = 0
    for (num in st) {
        res += num
    }
    return res
}

fun main() {
    var input = arrayOf("5", "2", "C", "D", "+")
    var output = calPoints(operations = input)
    println("output: $output, expected: 30")

    input = arrayOf("5", "-2", "4", "C", "D", "9", "+", "+")
    output = calPoints(operations = input)
    println("output: $output, expected: 27")
}