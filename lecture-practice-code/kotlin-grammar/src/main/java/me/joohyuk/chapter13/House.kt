package me.joohyuk.chapter13

fun main() {

}

class JavaHouse(
    private val address: String,
    private val livingRoom: LivingRoom
) {
    inner class LivingRoom(
        private val area: Double
    ) {
        val address: String
            get() = this@JavaHouse.address
    }
}