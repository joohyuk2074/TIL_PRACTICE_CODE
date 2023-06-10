package me.joohyuk.chapter14

fun main() {
    val person1 = PersonDto("김주혁", 100)
    val person2 = PersonDto("김주혁", 200)
}

data class PersonDto(
    val name: String,
    val age: Int
) {
}