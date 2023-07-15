package me.joohyuk.chapter09

fun main() {
    val person = Person("김주혁", 33)
}

class Person(
    val name: String,
    var age: Int
) {

    init {
        if (age <= 0) {
            throw IllegalArgumentException("나이는 ${age}일 수 없습니다.")
        }
        println("초기화 블록")
    }
}