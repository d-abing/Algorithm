class Solution {
    fun solution(numbers: IntArray): IntArray {
        val answer = IntArray(numbers.size) { -1 }
        val stack = mutableListOf<Int>()

        for (i in numbers.indices) {
            while (stack.isNotEmpty() && numbers[stack.last()] < numbers[i]) {
                val lastIdx = stack.removeLast()
                answer[lastIdx] = numbers[i]
            }
            stack.add(i)
        }

        return answer
    }
}
