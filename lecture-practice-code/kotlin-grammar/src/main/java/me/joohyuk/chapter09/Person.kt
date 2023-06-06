package me.joohyuk.chapter09

fun main() {
//    val person1 = Person("김주혁", 100)
//    println(person1.name)
//    person1.age = 10
//    println(person1.age)
//
//    val person2 = JavaPerson("김주혁", 100)
//    println(person2.name)
//    println(person2.age)
//
//    val person3 = Person("김주혁")

    val person = Person()
}

class Person(
    val name: String,
    var age: Int
) {

//    var name = name
//        set(value) {
//            field = value.uppercase()
//        }
//
//    fun getUppercaseName(): String {
//        return this.name.uppercase()
//    }
//
//    val uppercaseName: String
//        get() = this.name.uppercase()

    init {
        if (age <= 0) {
            throw IllegalArgumentException("나이는 ${age}일 수 없습니다.")
        }
        println("초기화 블록")
    }

    // 부 생성자보다는 주 생성자에서 초기화를 하거나 정적 팩토리 메서드를 쓴다.
    constructor(name: String) : this(name, 1) {
        println("첫 번째 부생성자")
    }

    constructor() : this("김주혁") {
        println("두 번째 부생성자")
    }

    // 객체의 속성이라면 Customer Getter권장 그렇지 않다면 함수로
    fun isAdul1(): Boolean {
        return this.age >= 20
    }

    // Custom getter방식
    val isAdult2: Boolean
        get() = this.age >= 20

    val isAdult3: Boolean
        get() {
            return this.age >= 20
        }
}