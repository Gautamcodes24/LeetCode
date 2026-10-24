class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_days(dt:str)->int:
            month = int(dt[:2])
            day = int(dt[3:])
            total_days = day
            for m in range(month-1):
                total_days += days[m]
            return total_days
        startA = to_days(arriveAlice)
        startB = to_days(arriveBob)
        endA = to_days(leaveAlice)
        endB = to_days(leaveBob)
        totalA = max(startA , startB)
        totalB = min(endA , endB)
        if totalA <= totalB:
            return totalB - totalA + 1
        return 0