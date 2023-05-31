package me.joohyuk.chapter03

fun main() {
    val number1 = 3
    val number2: Long = number1.toLong()

    val number3: Int? = 3
    val number4: Long = number3?.toLong() ?: 0L

    printAgeIfPerson2(null)


    val name = "김주혁"

    val str = """
        ABC
        EFG
        ${name}
    """.trimIndent()

    println(str)

    val str1 = "ABC"
    println(str1[0])
    println(str1[1])
    println(str1[2])
}

fun printAgeIfPerson1(obj: Any) {
    if (obj is Person) {
        println(obj.age)
    }
}

fun printAgeIfPerson2(obj: Any?) {
    val person = obj as? Person
    println(person?.age)
}
