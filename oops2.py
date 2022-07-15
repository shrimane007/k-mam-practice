### overriding of method-

# parent  class-

class abc:
    def __init__(self):
        print("tody is sunday")
    def bca(self):
        print("my  name ")
# .child class-

class mane(abc):
    def __init__(self):   
        # "constructor overriding"
        # super().__init__()
        print("python 2022")
    def xyz(self):
        print("i am shri,data scientist")
        
    def bca(self):     #method oerride.
        # super().bca()
        print("kksskkss")    
  
# make instance(of child class)-
# #if want to execute parent class also, use (super) key
a=mane()
a.xyz()
a.bca()



















































