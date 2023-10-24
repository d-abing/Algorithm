fun main() {
    var num = readLine()!!.toInt()
    var arr = readLine()!!.split(" ")
    val target = readLine()!!.toInt()
    var count = 0

    for (i in 0..num-1) {
        if (arr[i].toInt() == target) count++
    }
    println(count)
}