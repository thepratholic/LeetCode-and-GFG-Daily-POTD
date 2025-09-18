import heapq
from collections import defaultdict
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.task_map = defaultdict(tuple)

        for user_id, task_id, priority in tasks:
            heapq.heappush(self.pq, (-priority, -task_id, user_id))
            self.task_map[task_id] = (priority, user_id)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.pq, (-priority, -taskId, userId))
        self.task_map[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            user_id = self.task_map[taskId][1]
            self.task_map[taskId] = (newPriority, user_id)
            heapq.heappush(self.pq, (-newPriority, -taskId, user_id))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.pq:
            curr_priority, curr_taskId, curr_userId = heapq.heappop(self.pq)
            taskId = -curr_taskId
            priority = -curr_priority

            if taskId in self.task_map and self.task_map[taskId][0] == priority:
                userId = self.task_map[taskId][1]
                del self.task_map[taskId]
                return userId

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()