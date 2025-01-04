class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        
    def printLL(self):
        print("Node Data: ")
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def printHeadTail(self):
            if self.head is None:
                print("List is empty")
            else:
                print("Head: " + str(self.head.data))
                print("Tail: " + str(self.tail.data))

    def printTraverseLL(self):
        listofall = []
        curr = self.head
        while curr:
            listofall.append(curr.data)
            curr = curr.next
        print(listofall)

    def deleteNode(self, nodeindex):
        i = 1
        curr = self.head
        while i < nodeindex:
            i+=1
            curr = curr.next
        curr.next = curr.next.next
    
myLinked = LinkedList()
myLinked.insertAtBegin(5)
myLinked.insertAtBegin(10)
myLinked.insertAtBegin(15)
myLinked.insertAtBegin(20)
myLinked.insertAtEnd(4)
myLinked.insertAtEnd(3)
myLinked.insertAtEnd(2)
myLinked.insertAtEnd(1)

#myLinked.printHeadTail()
#myLinked.printLL()

myLinked.printTraverseLL()
myLinked.deleteNode(7)
myLinked.printTraverseLL()

