from collections import deque, defaultdict
from bisect import bisect_left, bisect_right, insort
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.storage = deque()            
        self.packet_set = set()         
        self.dest_map = defaultdict(list) 

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False

        if len(self.storage) >= self.memoryLimit:
            old_src, old_dest, old_ts = self.storage.popleft()
            self.packet_set.discard((old_src, old_dest, old_ts))

            arr_old = self.dest_map[old_dest]
            idx_old = bisect_left(arr_old, old_ts)
            if idx_old < len(arr_old) and arr_old[idx_old] == old_ts:
                arr_old.pop(idx_old)
            if not arr_old:
                del self.dest_map[old_dest]

        self.storage.append(packet)
        self.packet_set.add(packet)
        insort(self.dest_map[destination], timestamp)

        return True

    def forwardPacket(self) -> List[int]:
        if not self.storage:
            return []
        source, destination, timestamp = self.storage.popleft()
        self.packet_set.discard((source, destination, timestamp))

        arr = self.dest_map[destination]
        idx = bisect_left(arr, timestamp)
        if idx < len(arr) and arr[idx] == timestamp:
            arr.pop(idx)
        if not arr:
            del self.dest_map[destination]

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        arr = self.dest_map[destination]
        left = bisect_left(arr, startTime)
        right = bisect_right(arr, endTime)
        return right - left
