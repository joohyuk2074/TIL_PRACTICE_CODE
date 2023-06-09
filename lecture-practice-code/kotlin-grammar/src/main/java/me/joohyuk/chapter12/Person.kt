package me.joohyuk.chapter12

fun main() {
    println(Singleton.a)
    Singleton.a += 10
    println(Singleton.a)
}

class Person private constructor(
    var name: String,
    var age: Int
) {

    companion object Factory : Log {
        private const val MIN_AGE = 1   // const를 쓰면 컴파일 시 변수 할당
        fun newBaby(name: String): Person {
            return Person(name, MIN_AGE)
        }

        override fun log() {
            println("나는 Person 클래스의 동행객체 Factory에요")
        }
    }
}

object Singleton {
    var a: Int = 0
}