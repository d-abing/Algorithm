class Solution {
    fun solution(word: String): Int {
        var answer = 0
        var current = ""
        var order = listOf('A', 'E', 'I', 'O', 'U')
        
        while (current != word) {
            if (current.length == 5) {
                while (current.last() == 'U') {
                    current = current.dropLast(1)
                }
                val newLast = order[(order.indexOf(current.last()) + 1) % 5]
                current = current.dropLast(1) + newLast
            } else {
                current = current + 'A'
            }
            answer++
        }
        
        return answer
    }
}