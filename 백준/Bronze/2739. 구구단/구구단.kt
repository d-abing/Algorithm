fun main() {
    val num = readLine()!!.toInt()

    for ( i in 1..9) {
        println( "$num * $i = ${num * i}")
    }
}