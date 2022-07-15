# single level inheritanc


# class A:
#     def __init__(self):
#         print("constructor of class a")
#     def method1(self):
#         print("method 1 of clss a")    

# class B:

#     def __init__(self):
#         self.obj_a=A()
#         print("construcor of class b")

#     def method1 (self):
#         self.obj_a.method1()
#         print("method 1 of class b")   


# # obj_a=A()
# # obj_a.method1()
# obj_b=B()
# obj_b.method1()

#### multi level inheritance-

# class A:
#     def __init__(self):
#         print("constructor of class a")
#     def method1(self):
#         print("metho")

#     def method2(self):
#         print("method 2 of clas A")

# class B(A):

#     def __init__(self):
#         self.obj_a=A()
#         print("construcor of class b")

#     def method1 (self):
        
#         print("meth")   

# class C(B):
#     def __init__(self):
#         # print("constructor of class C")
#         pass
#     def method1(self):
#         # super(C,self).method1()
#         super(B,self).method1()
#         print("met") 

# c=C()
# c.method1()
# c.method2()
# obj_b=B()
# obj_b.metho

### multiple level inheriance- seperate class A & B

class A:
    def __init__(self):
        print("constructor of class a")
    def method1(self):
        print("metho")

    def method2(self):
        print("method 2 of clas A")

class B:

    def __init__(self):
        self.obj_a=A()
        print("construcor of class b")

    def method1 (self):
        
        print("meth")   

class C(A,B):
    def __init__(self):
        # print("constructor of class C")
        pass
    def method1(self):
        # super(C,self).method1()
        print(C.mro())

        super(C,self).method1()
        print("met") 
        # MRO - method resolution order-left to right

c=C()
c.method1()
# c.method2()
# obj_b=B()
# obj_b.metho

## dimond shape problem





























