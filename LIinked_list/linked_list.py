class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head

#if no head, new node-->head, else traverse till the end and add the element
    def append(self,new_node):
        current=self.head
        if current:
            while current.next:
                current=current.next
            current.next=new_node
        else:
            self.head=new_node

#Delete a node-->beg:self.head points to next node,other-->value traverse in while loop store previous, 
# if not found return else prev.next=current.next current=None

    def delete(self,value):
        current=self.head
        if current.data==value:
            self.head=current.next
        else:
            while current:
                if current.data==value:
                    break
                prev=current
                current=current.next
            if current==None:
                return
            prev.next=current.next
            current=None
#Insertion at beg-->easy, end-->easy inbewteen   -->position 1,2,3
    def insert(self,new_element,position):
        current=self.head
        if position==1:
            new_element.next=self.head
            self.head=new_element
        count=1
        while current:
            if count+1==position:
                new_element.next=current.next
                current.next=new_element
                return
            else:
                count+=1
                current=current.next
        pass
    
    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

l1=LinkedList(e1)

l1.append(e2)
l1.append(e3)
l1.append(e4)

l1.print()

e5= Node(2.5)

l1.insert(e5,3)
l1.print()

    