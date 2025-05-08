import kotlin.math.abs

class Solution {
    fun solution(n: Int, a: Int, b: Int): Int {
        var answer = 0
        var a = a
        var b = b
        
        while (a != b) {
            a = (a + 1) / 2
            b = (b + 1) / 2
            answer += 1
        }

        return answer
    }
}