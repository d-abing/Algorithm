class Solution {
    fun solution(s: String): IntArray {
        var str = s
        var change = 0
        var zero = 0
        
        while (str != "1") {
            zero += str.count { it == '0' }
            str = str.filter { it == '1' }
            
            var sum = str.length
            str = Integer.toBinaryString(sum)
            change ++
        }
        return intArrayOf(change, zero)
    }
}