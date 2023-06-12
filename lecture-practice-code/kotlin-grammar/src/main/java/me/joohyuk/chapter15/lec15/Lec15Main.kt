package me.joohyuk.chapter15.lec15


fun main() {

    val array = arrayOf(100, 200)
    for (i in array.indices) {
        println("${i} ${array[i]}")
    }

    array.plus(100)
    for ((idx, value) in array.withIndex()) {
        println("$idx $value")
    }

    val numbers = listOf(100, 200)      // 불변
    val number0 = numbers[0]
    val mutableListOf = mutableListOf(200, 100)    // 가변 리스트

    for (number in numbers) {
        println(number)
    }

    for ((idx, value) in numbers.withIndex()) {
        println("$idx $value")
    }


    val emptyList = emptyList<Int>()

    printNumbers(emptyList())


    mutableSetOf(100L)

    val oldMap = mutableMapOf<Int, String>()
    oldMap[1] = "MONDAY"
    oldMap[2] = "TUESDAY"

    for (key in oldMap.keys) {
        println(key)
        println(oldMap[key])
    }

    for ((key, value) in oldMap.entries) {
        println(key)
        println(value)
    }

    mapOf(1 to "MONDAY", 2 to "TUESDAY")
}

private fun printNumbers(numbers: List<Int>) {

}