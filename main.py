class Node:
    """
    This Node holds data value and next Node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.top = None
        self.botton = None
        self.length = 0
    def push(self, value: int):
        new_node = Node(value)
        if self.isEmpty:
            self.top = new_node
            self.botton = new_node
            self.length += 1
        else:
            holdingpointer = self.top
            self.top = new_node
            self.top.next = holdingpointer
            self.length += 1

        
    def pop(self):
        if self.top == None:
            return None

        holdingpointer = self.top
        self.top = holdingpointer.next
        self.length -= 1
        return holdingpointer.value
       
    def peek(self):
      if self.isEmpty:
        return None

      return self.top.value

    @property
    def isEmpty(self):
        return self.length == 0

    @property
    def items(self):
        if self.isEmpty:
            return []
        values = []
        current_node = self.top
        while current_node != None:
            values.append(current_node.value)
            current_node = current_node.next
        return values

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enqueued_data = Stack()
        self.dequeued_data = Stack()
        
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.dequeued_data.length != 0:
          self.enqueued_data.push(self.dequeued_data.pop())

        self.enqueued_data.push(x)

        while self.enqueued_data.length != 0:
          self.dequeued_data.push(self.enqueued_data.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.dequeued_data.isEmpty:
          return None

        return self.dequeued_data.pop()
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.dequeued_data.peek() == None:
          return None

        return self.dequeued_data.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """   
        return self.dequeued_data.isEmpty


queue = MyQueue();

queue.push(1);
queue.push(2);  
print(queue.peek()) 
print(queue.pop())
print(queue.pop()) 
print(queue.empty());