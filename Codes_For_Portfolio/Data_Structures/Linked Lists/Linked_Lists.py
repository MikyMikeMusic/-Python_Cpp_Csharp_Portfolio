class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
            
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
            
    def remove(self, data):
        if self.head is None:
           return
        
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        
        previous_node.next = current_node.next
        if self.tail == current_node:
            self.tail = previous_node
            
    def contains(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def insert_at(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.text = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = self.head
            return
        
        current_node = self.head
        current_index = 0
        while current_node and current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        if current_node is None:
            return
        
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
        if new_node.next is None:
            self.tail =new_node
             
# Test
MyList = LinkedList()
MyList.insert(1)
MyList.insert(2)
MyList.insert(3)
MyList.insert(4)
MyList.print_list()

MyList.remove(2)
MyList.print_list()

print(MyList.contains(2))

MyList.insert_at(3, 4)
MyList.print_list()

       
        
