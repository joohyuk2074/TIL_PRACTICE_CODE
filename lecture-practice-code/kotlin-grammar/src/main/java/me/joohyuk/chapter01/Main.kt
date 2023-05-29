package me.joohyuk.chapter01

import me.joohyuk.chapter01.Main.Person

fun main() {
    // 1. 변수 선언

    // mutable한 변수 선언
    var number1 = 10L

    // immutable한 변수 선언
    val number2 = 10L

    // 타입 명시적인 mutable한 변수 선언
    var number3: Long = 10L

    // 타입 명시적인 immutable한 변수 선언
    val number4: Long = 10L

    /**
     * 모든 변수는 우선 val로 만들고 필요한경우에 var로 변경한다
     */

    // 2. Kotlin에서의 Primitive Type
    var number5 = 10L
    var number6 = 1_000L

    // 3. nullable 변수 표현
    var number7: Long? = 1_000L
    number7 = null

    // 4. 객체 인스턴스화
    var person = Person("김주혁")
}