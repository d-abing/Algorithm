class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer = intArrayOf()

        val release = progresses.mapIndexed { idx, value -> value to speeds[idx] }
        val days = mutableListOf<Int>()

        for ((progress, speed) in release) {
            var neededDay = ((100 - progress) + speed - 1) / speed
            days.add(neededDay)
        }

        var count = 0
        var previous = days[0] 

        while (days.isNotEmpty()) {
            val current = days[0]

            if (current <= previous) {
                count++
            } else {
                answer = answer.plus(count)
                count = 1
                previous = current
            }

            days.removeAt(0)
        }

        answer = answer.plus(count)
        return answer
    }
}
