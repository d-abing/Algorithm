fun main() {
    val dice = readLine()!!.split(" ")
    val dice1 = dice[0].toInt()
    val dice2 = dice[1].toInt()
    val dice3 = dice[2].toInt()
    var msg : Int

    if ( dice1 == dice2 && dice2 == dice3 ) {
        msg = 10000 + dice1 * 1000
    } else if ( dice1 == dice2 || dice1 == dice3 ) {
        msg = 1000 + dice1 * 100
    } else if ( dice2 == dice3 ) {
        msg = 1000 + dice2 * 100
    } else {
        val max = if ( dice1 > dice2 && dice1 > dice3) dice1 else if ( dice2 > dice3 ) dice2 else dice3
        msg = max * 100
    }

    println(msg)
}