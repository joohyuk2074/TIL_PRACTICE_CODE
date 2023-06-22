package me.joohyuk.chapter20

import me.joohyuk.chapter03.Person

fun main() {

}

fun printPerson(person: Person?) {
    person?.let {
        println(it.name)
        println(it.age)
    }
}