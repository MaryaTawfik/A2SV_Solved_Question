from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value =value
        self.k=k
        

    def consec(self, num: int) -> bool:
        # self.value =value
        # self.k=k
        self.queue.append(num)
        if num != self.value:
            while self.queue and self.queue[0]!= num:
                self.queue.popleft()
            self.queue.pop()
        if len(self.queue) == self.k:
            self.queue.popleft()
            return True
        else :
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)