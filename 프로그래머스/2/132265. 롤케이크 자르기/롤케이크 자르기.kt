class Solution {
    fun solution(topping: IntArray): Int {
        val leftSet = mutableSetOf<Int>()
        val rightMap = mutableMapOf<Int, Int>()

        for (t in topping) {
            rightMap[t] = rightMap.getOrDefault(t, 0) + 1
        }

        var answer = 0
        for (i in 0 until topping.size - 1) {
            val now = topping[i]

            leftSet.add(now)
            
            rightMap[now] = rightMap[now]!! - 1
            if (rightMap[now] == 0) {
                rightMap.remove(now)
            }

            if (leftSet.size == rightMap.size) {
                answer++
            }
        }
        return answer
    }
}