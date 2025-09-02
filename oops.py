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


# test
# class Student:
#     def __init__(self,name,mat,phy,che):
#         self.name=name
#         self.mat=mat
#         self.phy=phy
#         self.che=che 
#     def average(self):
#         avg=(self.mat+self.phy+self.che )/3
#         # print(avg)
#         return avg
#         # return self.avg/3

# s1=Student("kiran",99,98,97)
# # s1.average()
# print(s1.average())


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks 
    
#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print(self.name,"average is",sum/3)
    
# s1=Student("kiran",[99,98,97])
# s1.average()
# s1.name="surya"
# s1.average()


# ABSTRACTION= Hiding the implementation details of class, only showing the essential details to user(avoding unnecessary)
# class car:
#     def __init__(self):
#         self.acc=False
#         self.bre=False
#         self.clu=False
    
#     def start(self):
#         self.clu=True
#         self.acc=True
#         print("car started...")
# s1=car()
# s1.start()


# ENCAPSULATION = Wrapping data and functions into single unit(object)


# Pratice
class Acount:
    def __init__(self,accno,bal):
        self.accno=accno
        self.bal=bal
    
    def debit(self,amount):
        self.bal-=amount
        print("Rs",amount,"was debited")
        print("total balance =",self.get_balance())

    def credit(self,amount):
        self.bal+=amount
        print("Rs",amount,"was credited") 
        print("total balance =",self.get_balance())   
    
    def get_balance(self):
        return self.bal
        
acc1=Acount(123456,10000)
acc1.debit(500)
acc1.credit(1000)
































































