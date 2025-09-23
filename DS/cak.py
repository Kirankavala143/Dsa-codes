import calendar as cal

for i in range(1, 13):
    print(cal.month(2025,i))


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None



# class Stack:
#     def __init__(self):
#         self.head=None
#     def push(self,data):
#         newNode=Node(data)
#         if self.head==None:
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode
#     def isEmpty(self):
#         return self.head==None
#     def pop(self):
#         if self.isEmpty():
#             print("stack is Empty")
            
#         else:
#             self.head=self.head.next
#     def peek(self):
#         if self.isEmpty():
#             print("stack is Empty")
#         else:
#             return self.head.data
    
# st=Stack()
# st.push(1)
# st.push(2)
# st.pop()
# print(st.peek())

# class Solution:
#     def isValid(self, s: str) -> bool:
#         st=[]
#         for ch in s:
#             if ch in "([{":
#                 st.append(ch)
#             else:
#                 if(len(st)==0):
#                     return False
#                 ch2=st.pop()
#                 if ch==")":
#                     if ch2=="(":
#                         continue
#                     else:
#                         return False
#                 elif ch=="]":
#                     if ch2=="[":
#                         continue
#                     else:
#                         return False
#                 else:
#                     if ch2=="{":
#                         continue
#                     else:
#                         return False
#         if len(st)==0:
#             return True
#         else:
#             return False

class Stack:

    def __init__(self):
        self.st=[]
    def push(self,data):
        self.st.append(data)
    def isEmpty(self):
        if len(self.st)==0:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.st.pop()
    def peek(self):
        if self.isEmpty():
            print("No Element exist in stack")
        else:
            return self.st[-1]
        
st=Stack()
st.push(1)
print(st.peek())
st.pop()
st.peek()

