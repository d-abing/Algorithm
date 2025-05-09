class Solution {
    fun solution(want: Array<String>, number: IntArray, discount: Array<String>): Int {
        var answer: Int = 0
        
        val products = want.mapIndexed { idx, value -> value to number[idx] }
        
        for (i in 0..discount.size - 10) {
            var canBuy = true
            val current = discount.slice(i until i + 10)
            for ((want, number) in products) {
                if (current.count { it == want} != number) {
                    canBuy = false
                    break
                }
            }
            if (canBuy) {
                answer += 1
            }
        }
        
        return answer
    }
}