class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
    
    def __str__(self) -> str:
        if self.val is None:
            return("Empty")
        currentNode = self
        mystr = ""
        while currentNode:
            mystr += (str(currentNode.val)+',')
            currentNode = currentNode.next
        mystr = mystr[0:len(mystr)-1:1]
        return (f"[{mystr}]")

#[9,9,9,9,9,9,9]
#l1 = ListNode(9)
#l1.next = ListNode(9)
#l1.next.next = ListNode(9)
#l1.next.next.next = ListNode(9)
#l1.next.next.next.next = ListNode(9)
#l1.next.next.next.next.next = ListNode(9)
#l1.next.next.next.next.next.next = ListNode(9)

#[9,9,9,9]
#l2 = ListNode(9)
#l2.next = ListNode(9)
#l2.next.next = ListNode(9)
#l2.next.next.next = ListNode(9)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(9)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)


result = None
carry = 0

while l1 is not None or l2 is not None:
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    sum = val1 + val2 + carry
    carry = 0

    if sum > 9:
        sum -= 10
        carry = 1

    if not result:
        result = ListNode(sum)
        current_node = result
    else:
        current_node.next = ListNode(sum)
        current_node = current_node.next

    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
    

if carry > 0:
    current_node.next = ListNode(1)

print(result)