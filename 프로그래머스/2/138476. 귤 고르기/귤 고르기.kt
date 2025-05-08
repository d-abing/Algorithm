class Solution {
    fun solution(k: Int, tangerine: IntArray): Int {
        var answer: Int = 0
        
        var k = k
        var tangerineCountMap = mutableMapOf<Int, Int>()
        
        for (i in tangerine) {
            if(i in tangerineCountMap) {
                continue
            } else {
                tangerineCountMap[i] = tangerine.count{ it == i }
            }
        }
        
        val countList = tangerineCountMap.values.sortedDescending()
        
        for (i in countList) {
           if (k > 0) {
               k -= i
               answer += 1
           } else {
               break
           }
        }
        
        return answer
    }
}