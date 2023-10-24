fun main() {
    val x = readLine()!!.toInt()
    val y = readLine()!!.toInt()
    var msg = ""
    when {
        x > 0 && y > 0 -> msg = "1"
        x < 0 && y > 0 -> msg = "2"
        x < 0 && y < 0 -> msg = "3"
        else -> msg = "4"
    }
    println(msg)
}
