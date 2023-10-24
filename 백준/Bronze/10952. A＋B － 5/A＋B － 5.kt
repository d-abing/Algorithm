fun main() {
    while (true) {
        val num = readLine()!!.split(" ")
        val a = num[0].toInt()
        val b = num[1].toInt()
        if (a == 0 && b == 0) {
            break
        } else {
            println(a + b)
        }
    }
}