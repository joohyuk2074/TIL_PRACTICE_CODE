package me.joohyuk.chapter04

fun main() {
    val money1 = JavaMoney(2_000L)
    val money2 = JavaMoney(1_000L)

    // Java와 다르게 객체를 비교할때 비교 연산자를 사용하면 자동으로 compareTo를 호출해줍니다.
    if (money1 > money2) {
        println("Money1이 Money2보다 금액이 큽니다.")
    }

    val money3 = JavaMoney(1_000L)
    val money4 = money3
    val money5 = JavaMoney(1_000L)

    println(money3 === money4)      // 동일성
    println(money3 == money5)       // 동등성
    println(money3 === money5)

    val javaMoney6 = money3 + money5 // 연산자 오버로딩
    println(javaMoney6)
}

