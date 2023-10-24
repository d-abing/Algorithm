fun main() {
    val nx = readLine()!!.split(" ")
    val n = nx[0].toInt()
    val x = nx[1].toInt()
    var arr = readLine()!!.split(" ")
    var result = ""

    for (i in 1..n) {
        if (arr[i-1].toInt() < x) result += " "  + arr[i-1]
    }
    println(result.substring(1))
}