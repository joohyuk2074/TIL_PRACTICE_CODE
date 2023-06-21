package me.joohyuk.chapter19

class Person(
    val name: String,
    val age: Int
) {
    operator fun component1(): String {
        return this.name
    }

    operator fun component2(): Int {
        return this.age
    }
}

fun main() {
    val person = Person("김주혁", 100)
    val (name, age) = person
//    val name = person.component1()
//    val age = person.component2()

    println("이름: ${name}, 나이: ${age}")

    val numbers = listOf(1, 2, 3)
    numbers.map { number -> number + 1 }
        .forEach { number -> println(number) }

    run {
        numbers.forEach { number ->
            if (number == 2) {
                return@forEach
            }
        }
    }

    // 별로 추천 x
    abc@ for (i in 1..100) {
        for (j in 1..100) {
            if (j == 2) {
                break@abc
            }
        }
    }
}

fun getNumberOrNullV2(): Int? {
    val number: Int = 123
    return number.takeIf { it > 0 }
}