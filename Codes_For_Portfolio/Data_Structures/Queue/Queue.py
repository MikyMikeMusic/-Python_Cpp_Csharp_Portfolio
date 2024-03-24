from Node import Node


class Queue:
    def __init__(self):
        self.front = self.rear = None
        
    def is_Empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.rear is None:
            self.front = self.rear = new_node
            return
        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.is_Empty():
            return
        new_node = self.front
        self.front = new_node.next
        if self.front is None:
            self.front.prev = None
        if self.front is None:
            self.rear = None
        return new_node.data
    
    def peek(self):
        if self.is_Empty():
            return
        return self.front.data
    
    def get_rear(self):
        if self.is_Empty():
           return None
        return self.rear.data
    


       
     
        
    




