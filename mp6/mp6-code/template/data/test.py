import queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.flag = True

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.flag:
            self.q2.put(x)
            l = self.q1.qsize()
            print(l)
            while l:
                self.q2.put(self.q1.get())
                l -= 1
        else:
            self.q1.put(x)
            l = self.q1.qsize()
            print(l)
            while l:
                self.q1.put(self.q2.get())
                l -= 1
        self.flag = -self.flag

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.flag:
            return self.q1.get()
        else:
            return self.q2.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.flag:
            element = self.q1.get()
            self.q1.put(element)
            return element
        else:
            element = self.q2.get()
            self.q2.put(element)
            return element

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.flag:
            return self.q1.qsize == 0
        else:
            return self.q2.qsize == 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(10)
obj.push(15)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(111111)
print(param_2,param_3,param_4)