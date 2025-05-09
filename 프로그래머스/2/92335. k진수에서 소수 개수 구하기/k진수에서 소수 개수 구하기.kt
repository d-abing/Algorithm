import kotlin.math.sqrt

class Solution {
    fun solution(n: Int, k: Int): Int {
        val num = n.toString(k)
        val numbers = num.split('0')
            .filter { it.isNotBlank() }
            .mapNotNull { it.toLongOrNull() }

        return numbers.count { isPrime(it) }
    }

    fun isPrime(n: Long): Boolean {
        if (n < 2) return false
        if (n == 2L) return true
        if (n % 2 == 0L) return false

        val sqrtN = sqrt(n.toDouble()).toLong()
        for (i in 3..sqrtN step 2) {
            if (n % i == 0L) return false
        }
        return true
    }
}
