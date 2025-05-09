class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        var answer = 0
        
        val map = mutableMapOf<String, Int>()

        for ((_, type) in clothes) {
            map[type] = map.getOrDefault(type, 0) + 1
        }

        return map.values.fold(1) { acc, count -> acc * (count + 1) } - 1
    }
}