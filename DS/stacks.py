# STACKS
# LIFO (Last In, First Out)

# The two main operations:
# 1)push(x) → Add element on top.
# 2)pop() → Remove and return the top element.

# Other common ones:
# 1)peek()/top() → See the top element without removing it.
# 2)isEmpty() → Check if stack is empty.
# 3)size() → Number of elements.

#list as stack
# s=[] 
# s.append(10)
# s.append(20)
# s.append(30)
# print(s)
# print(s.pop()) #pop
# print(s)
# print(s[-1]) #peek
# print(len(s)) #size
# print(len(s)==0) #isEmpty

# STACKS
# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         raise IndexError("pop from empty stack")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         raise IndexError("peek from empty stack")

#     def size(self):
#         return len(self.items)

#     def __str__(self):
#         return str(self.items) # string representation of the stack

# # Example usage:
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s)          # [1, 2, 3]
# print(s.pop())    # 3
# print(s.peek())   # 2
# print(s.size())   # 2
# print(s.is_empty())  # False
# print(s.pop())    # 2
# print(s.pop())    # 1
# print(s.is_empty())  # True

# Linked List as stack
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None

#     def isEmpty(self):
#         return self.top is None

#     def push(self, data):
#         newnode = Node(data)
#         newnode.next = self.top
#         self.top = newnode

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#             return None
#         popped = self.top.data
#         self.top = self.top.next
#         return popped

#     def peek(self):
#         if self.isEmpty():
#             return None
#         return self.top.data

#     def getSize(self):
#         count=0
#         temp=self.top
#         while temp:
#             count+=1
#             temp=temp.next
#         return count

#     def reverse(self):
#         prev=None
#         curr=self.top
#         while curr!=None:
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
#         self.top=prev


#     def printStack(self):
#         temp = self.top
#         while temp:
#             print(temp.data, "->", end=" ")
#             temp = temp.next
#         print("None")

# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.printStack()   # 30 -> 20 -> 10 -> None
# print("Popped:", s.pop())   # 30
# print("Top:", s.peek())     # 20
# print("Is Empty:", s.isEmpty()) # False
# print("Size:", s.getSize()) # 2
# s.printStack()   # 20 -> 10 -> None
# s.reverse()
# s.printStack()   # 10 -> 20 -> None


# Reverse a stack
# s="kiran"
# stack=[]
# for i in s:
#     stack.append(i)
# rev=""
# while stack:
#     rev+=stack.pop()
# print(rev)

# def is_balanced_simple(s):
#     count = 0
#     for ch in s:
#         if ch == '[':
#             count += 1
#         elif ch == ']':
#             count -= 1
#             if count < 0:  # more closing than opening
#                 return False
#     return count == 0

# # Test
# print(is_balanced_simple("[]"))     # True
# print(is_balanced_simple("[[]"))    # False
# print(is_balanced_simple("[[]]"))    # False

def is_balanced_stack(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":              # opening bracket
            stack.append(ch)         # push
        elif ch in ")}]":            # closing bracket
            if not stack or stack[-1] != mapping[ch]:
                return False         # mismatch
            stack.pop()              # valid pair, pop
    return not stack
# Test
print(is_balanced_stack("([{}])"))        # True
print(is_balanced_stack("([]{}"))       # False
print(is_balanced_stack("()[]{}"))      # True


def eval_postfix(expr):
    stack = []
    for ch in expr.split():
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b, a = stack.pop(), stack.pop()
            if ch == '+': stack.append(a+b)
            elif ch == '-': stack.append(a-b)
            elif ch == '*': stack.append(a*b)
            elif ch == '/': stack.append(int(a/b))
    return stack[0]
# Test
print(eval_postfix("3 4 + 2 * 7 /"))  # 2
print(eval_postfix("5 1 2 + 4 * + 3 -"))  # 14
