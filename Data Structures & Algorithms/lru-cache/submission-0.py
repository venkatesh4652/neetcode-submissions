class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.deq = deque()
        self.m = dict()

    def get(self, key: int) -> int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key not in self.m:
            if len(self.m) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)
        self.deq.append(key)
        self.m[key] = value
