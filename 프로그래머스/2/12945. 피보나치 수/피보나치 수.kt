class Solution {
    var fibonacciMap = mutableMapOf<Int, Int>(
            0 to 0,
            1 to 1
        ) 
    
    fun solution(n: Int): Int {
        return fibonacci(n)
    }
    
    
    fun fibonacci(n: Int): Int {
        if (n !in fibonacciMap) {
            fibonacciMap[n] = (fibonacci(n - 2) + fibonacci(n - 1))  % 1234567
        }
        return fibonacciMap[n]!!
    }
}
