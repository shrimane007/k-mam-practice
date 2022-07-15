# oops-
# procedure,object oriented 
# functions within class(method)

# class classroom:
#     statment-1

#     statmment-2
# class = init method
# self=act as pointer


# class Printit:
#     def _init_(self,y):
#         self.y=y
#         print("y:",y)
#     def prin(self,x):
#         self.x=x
#         print("x:",x)

# obj=Printit(15)
# obj.prin(10)



# class shri:
#     def __init__(self,x,y,z):
#         self.x=x 
#         self.y=y 
#         self.z=z 
#         print("self x:",x)
#         print(y)
#         print(z)
        
        

# obj=shri(10,12,13)

# revision

# class shri:
#     stmnt-1
# #     stmnt-2

# class mane:
#     def __init__(ss) :
#       pass
#     def abc(ss):
#         print("i am shrii")

# # making instance()

# obj=mane()
# obj.abc()
# (ss)/(self) should be same in init() and abc()
# bybdefault self is first parameter.

# class me:
#     def __init__(self,y,v,h) :
#       self.y=y
#       self.v=v
#       self.h=h    
#       print("y:",y,"v:",v,"h:",h)
#       print(y,v,h)
#     def abc(self,x):
#         self.x=x
#         print("x:",x)
#     def ggg(self,f) :
#         self.f=f
#         print("f:",f)

# obj=me(15,20,58)
# obj.abc(10)
# obj.ggg(5555)

class dhanu:
    # constructor overloading-
    # def __init__(self):
    #     pass

    # def ___init__(self,x):
    #     print()
# problem solving of constr.overloading-
    # def __init__(self,x=10,y=20):
    #     print(x+y)
    def __init__(self,*x):
        print(sum(x))

        # self.x=x
        # self.y=y
        # a=int(input("first no:"))
        # b=int(input("second no:"))
        # print("total no:",(a+b))
        # print(x)
        # print(y)
# metho overloading-

    # def abc(self): 
    #     print()
# solving problem of method overloading:
#1- using variable arg:
    # def abc(self,*a):
    #     print(sum(a))  

    # def abc(self,a,b):
    #     print(self,a,b)       

# 2-using default arg-
    # def abc(self,a=11,b=22):
    #     print(a+b)

obj=dhanu()
obj=dhanu(50)
# obj.abc(45)
obj=dhanu(100,200) 
# obj.abc(48,65)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@gmail.com'

    def full_name(self):
        return f'{self.first} {self.last}'


obj_=Employee ('John', 'Smith')
print(obj_.first)
print(obj_.email)
print(obj_.full_name())
print('-------------------------------------')

# but if we change first name then first name will change but email will take old first name
obj_.first = 'Tim'
print(obj_.first)
print(obj_.email)
print(obj_.full_name())
print('-------------------------------------')





