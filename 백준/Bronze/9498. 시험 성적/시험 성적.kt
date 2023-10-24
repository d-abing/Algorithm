fun main() {
    val input = readLine()!!.toInt()
    var msg = ""
    when {
        input >= 90 -> msg = "A"
        input >= 80 -> msg = "B"
        input >= 70 -> msg = "C"
        input >= 60 -> msg = "D"
        else -> msg = "F"
    }
    println(msg)
}
