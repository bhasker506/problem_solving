from queue import Queue

class Stack:
    
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, num:int):
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        
        self.q1.put(num)
        
        while not self.q2.empty():
            self.q1.put(self.q2.get())
    
    def pop(self) -> int:
        if self.q1.empty():
            raise Exception
        return self.q1.get()
    
    def top(self) -> int:
        if self.q1.empty():
            raise Exception
        return self.q1.queue[0]
    
    def size(self):
        return self.q1.qsize()


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(11)
    s.push(12)
    print(s.pop())
    print(s.pop())
    print(s.pop())