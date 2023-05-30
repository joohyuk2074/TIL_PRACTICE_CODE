package me.joohyuk.chapter02

fun main() {

    // Safe Call
    val str1: String? = "ABC"
    println(str1?.length)

    // Elvis 연산자
    val str2: String? = null
    println(str2?.length ?: 0)

    val startWithA4 = startWithA4("ABC")
    println(startWithA4)

    val person = Person("공부하는 개발자")
    startWithA(person.name)
}

fun startWithA(str: String): Boolean {
    return str.startsWith("A")
}

fun startWithA1(str: String?): Boolean {
    return str?.startsWith("A")
        ?: throw IllegalArgumentException("null이 들어왔습니다")
}

fun startWithA2(str: String?): Boolean? {
    return str?.startsWith("A")
}

fun startWithA3(str: String?): Boolean {
    return str?.startsWith("A") ?: false
}

fun startWithA4(str: String?): Boolean {
    return str!!.startsWith("A")
}