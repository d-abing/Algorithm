class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        
        val sorted = citations.sortedDescending()
        
        for (h in citations.size downTo 0) {
            if (h <= sorted.count { it >= h }) {
                answer = h
                break
            }
        }
        
        return answer
    }
}