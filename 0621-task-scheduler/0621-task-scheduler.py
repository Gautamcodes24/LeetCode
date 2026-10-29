from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)
        colling_period = deque()
        time = 0
        while colling_period or maxHeap:
            time += 1
            if not maxHeap:
                time = colling_period[0][1]
            else:
                remaning_task = 1 + heapq.heappop(maxHeap)
                if remaning_task:
                    colling_period.append((remaning_task,time+n))
            if colling_period and colling_period[0][1] == time:
                heapq.heappush(maxHeap,colling_period.popleft()[0])
        return time
                
        