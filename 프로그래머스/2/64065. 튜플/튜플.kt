class Solution {
    fun solution(s: String): IntArray {
        var answer = intArrayOf()
        
        var outerList = s
                    .removePrefix("{{")
                    .removeSuffix("}}")
                    .split("},{")
                    .map { it.split(",").map { it.toInt() } }
                    .sortedBy { it.size }
        
        var previous = listOf<Int>()
        
        for (list in outerList) {
            for (num in list) {
                if (num !in previous) {
                    answer += num
                }
            }
            previous = list
        }
        
        return answer
    }
}