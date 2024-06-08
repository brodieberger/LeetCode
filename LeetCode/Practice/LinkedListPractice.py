class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
myLinked = LinkedList()
myLinked.insertAtBegin(5)
myLinked.insertAtBegin(10)
myLinked.insertAtBegin(15)
myLinked.insertAtBegin(20)

print("Node Data: ")
myLinked.printLL()