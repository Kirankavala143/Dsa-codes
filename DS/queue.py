# <!-- QUEUES:
# A Queue is a linear data structure that follows the FIFO (First In First Out) principle.

# 2. Basic Operations in Queue
# 1)Enqueue (Insertion) → Add element to the rear of the queue.
# 2)Dequeue (Deletion) → Remove element from the front of the queue.
# 3)Peek/Front → Get the first element without removing it.
# 4)isEmpty → Check if queue is empty.
# 5)isFull → (for fixed-size arrays) check if queue is full.

# 3. Types of Queues
# 1)Simple Queue (Linear Queue)
#        1)FIFO.
#        2)Insert at rear, delete from front.
# 2)Circular Queue
#         Last position connects to first → avoids wasted space in simple queue.
# 3)Double-Ended Queue (Deque)
#         Insertion/deletion can be done from both ends.
# 4)Priority Queue
#         Each element has a priority.
#         Higher priority elements are served first. -->

# list as queue
# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         raise IndexError("dequeue from empty queue")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         raise IndexError("peek from empty queue")

#     def size(self):
#         return len(self.items)

#     def __str__(self):
#         return str(self.items)  # string representation of the queue    

# # Example usage:
# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print(queue)  # Output: [10, 20, 30]
# print(queue.peek())  # Output: 10
# print(queue.dequeue())  # Output: 10
# print(queue)  # Output: [20, 30]
# print(queue.is_empty())  # Output: False
# print(queue.size())  # Output: 2

# linked list as queue
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def is_empty(self):
#         return self.front is None

#     def enqueue(self, item):
#         new_node = Node(item)
#         if self.rear:
#             self.rear.next = new_node
#         self.rear = new_node
#         if not self.front:
#             self.front = new_node

#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("dequeue from empty queue")
#         removed_data = self.front.data
#         self.front = self.front.next
#         if not self.front:
#             self.rear = None
#         return removed_data

#     def peek(self):
#         if self.is_empty():
#             raise IndexError("peek from empty queue")
#         return self.front.data

#     def size(self):
#         count = 0
#         current = self.front
#         while current:
#             count += 1
#             current = current.next
#         return count
    
#     def reverse(self):
#         prev=None
#         curr=self.front
#         while curr!=None:
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
#         self.front=prev

#     def print_queue(self):
#         current = self.front
#         elements = []
#         while current:
#             elements.append(current.data)
#             current = current.next
#         print("Queue:", " -> ".join(map(str, elements)))

# # Example usage:
# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)   
# queue.enqueue(30)
# queue.print_queue()  # Output: Queue: 10 -> 20 -> 30
# print(queue.peek())  # Output: 10
# print("Dequeued:", queue.dequeue())  # Output: 10
# print(queue.is_empty())  # Output: False
# print(queue.size())  # Output: 2
# queue.reverse()
# queue.print_queue()  # Output: Queue: 30 -> 20



































