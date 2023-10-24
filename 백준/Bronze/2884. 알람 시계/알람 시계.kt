fun main() {
    val original = readLine()!!.split(" ")
    val h = original[0].toInt()
    val m = original[1].toInt()
    var changedH : Int
    var changedM : Int
    if (h < 1 && m < 45) {
        changedH = 23
        changedM = 60 + (h * 60 + m - 45) % 60
    } else {
        changedH = (h * 60 + m - 45) / 60
        changedM = (h * 60 + m - 45) % 60
    }
    var msg = "$changedH $changedM"
    println(msg)
}
