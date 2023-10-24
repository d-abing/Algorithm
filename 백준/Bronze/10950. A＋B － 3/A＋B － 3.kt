fun main() {
    val num = readLine()!!.toInt()

    for ( i in 1..num) {
        val target = readLine()!!.split(" ")
        val a = target[0].toInt()
        val b = target[1].toInt()
        println( "${a + b}")
    }
}
