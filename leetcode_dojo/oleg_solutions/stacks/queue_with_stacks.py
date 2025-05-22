# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def push(self, x: int) -> None:
        self.__stack1.append(x)
        
    def pop(self) -> int:
        while(len(self.__stack1)>0):
            self.__stack2.append(self.__stack1.pop())
        ans = self.__stack2.pop()
        while(len(self.__stack2)>0):
            self.__stack1.append(self.__stack2.pop())
        return ans
        
    def peek(self) -> int:
        return 0 if len(self.__stack1)==0 else self.__stack1[0]

    def empty(self) -> bool:
        return len(self.__stack1) == 0
    
    

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()