class Solution {
    fun solution(s: String): String {
        val numbers = s.split(" ").map { it.toInt() }
        val min = numbers.minOrNull()!!
        val max = numbers.maxOrNull()!!
        return "$min $max"
    }
}