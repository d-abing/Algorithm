import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun main() {
    var bw = BufferedWriter(OutputStreamWriter(System.`out`))

    for (i in 1 .. readLine()!!.toInt()) {
        var V1 = readLine()!!.split(" ");
        bw.write("Case #$i: ${V1[0].toInt() + V1[1].toInt()} \n")
    }
    bw.flush()
}