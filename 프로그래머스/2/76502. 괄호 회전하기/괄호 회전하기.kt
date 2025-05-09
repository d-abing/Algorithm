class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        
        // "[](){}[](){"
        // "}]()[{}]()["
        val str = (s + s).take(s.length * 2 - 1)
        
        for (i in 0..(str.length - s.length)) {
            var isCorrect = true
            val sliceStr = str.slice(i until (s.length + i))
            val stack = ArrayDeque<Char>()
            
            for (j in sliceStr) {
                if(j == '[' || j == '{' || j == '(') {
                    stack.addLast(j)
                } else if (stack.isNotEmpty()) {
                    val last = stack.last()
                    when (j) {
                        ']' -> {
                            if(last != '[') {
                                isCorrect = false 
                                break
                            } else {
                                stack.removeLast()
                            }
                        }
                        '}' -> {
                            if(last != '{') {
                                isCorrect = false 
                                break
                            } else {
                                stack.removeLast()
                            }
                        }
                        ')' -> {
                            if(last != '(') {
                                isCorrect = false 
                                break
                            } else {
                                stack.removeLast()
                            }
                        }
                    }
                } else {
                    isCorrect = false
                    break
                }
            }
            if (isCorrect && stack.isEmpty()) {
                answer += 1
            }
        }
        
        return answer
    }
}