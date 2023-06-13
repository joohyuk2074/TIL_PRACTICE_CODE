package me.joohyuk.chapter16

fun main() {
    val str = "ABC"
    val lastChar = str.lastChar()
    println(lastChar)
}

fun String.lastChar(): Char {
    return this[this.length - 1]
}