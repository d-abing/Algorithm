class Solution {
    fun solution(arr: IntArray): Int {
        return lcmOfList(arr.toList())
    }
    
    fun gcd(a: Int, b: Int): Int {
        return if (b == 0) a else gcd(b, a % b)
    }

    fun lcm(a: Int, b: Int): Int {
        return a * b / gcd(a, b)
    }

    fun lcmOfList(numbers: List<Int>): Int {
        return numbers.fold(1) { acc, num -> lcm(acc, num) }
    }
}