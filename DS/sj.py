class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None 
        
    def isempty(self):
        return self.head == None and self.tail==None
        
    def addfirst(self,data):
        newnode=Node(data)
        if self.isempty():
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def addlast(self,data):
        newnode=Node(data)
        if self.isempty():
            self.head=newnode
            self.tail=newnode 
        else:
            self.tail.next=newnode 
            self.tail=newnode 
        
    def addmiddle(self,prevnode,data):
        if prevnode is None:
            print("The given previous node cannot be NULL")
            return
        newnode=Node(data)
        newnode.next=prevnode.next
        prevnode.next=newnode
    def printdata(self):
        if self.isempty():
            print("Linked list is empty")
            return
        temp=self.head
        while temp!=None:
            print(temp.data,"->",end=" ")
            temp=temp.next
        print("None")

s1=LinkedList()
s1.addfirst(3)
s1.addfirst(4)
s1.addfirst(5)
s1.printdata()
s1.addlast(9)
s1.addlast(8)
s1.printdata()