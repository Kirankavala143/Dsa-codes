# class Student:
#     name="kiran"

# s1=Student()
# print(s1.name)

# class Student:
#     college="abc" #class atr
#     def __init__(self,name,marks):
#         self.name=name   # obj atr
#         self.marks=marks
#         print("Hi,hello")
# s1=Student("kiran",89)
# print(s1.name,s1.marks)
# print(s1.college)

# class Student:
#     college="abc" #class atr
#     def __init__(self,name,marks):
#         self.name=name   # obj atr
#         self.marks=marks
#         print("Hi,hello")
    
#     def welcome(self):           #methods=functions        
#         print("welcome sir",self.name)
    
#     def get_marks(self):
#         return self.marks

# s1=Student("kiran",89)
# s1.welcome()
# print(s1.get_marks())
# # print(s1.name,s1.marks)
# # print(s1.college)


class Student:
    def __init__(self,name,mat,phy,che):
        self.name=name
        self.mat=mat
        self.phy=phy
        self.che=che 
    
    def average(self,avg):
        self.avg=self.mat+self.phy+self.che 
        print(self.avg/3)
        # return self.avg/3

s1=Student("kiran",[45,46,48])
s1.average()
# print(s1.average())








