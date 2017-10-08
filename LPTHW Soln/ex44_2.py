class Parent(object):
    """docstring for ."""
    def __init__(self,var):
        print("This was Parent1 Class Called",var)

    def altered(self):
        #super(, self).__init__()
        #self.arg = arg
        print("1.PARENT altered()")
    def pri(self):
        print("Hello World!")

class Parent2(object):
    """docstring for ."""
    def trythis(self,var):
        #super(, self).__init__()
        #self.arg = arg
        print("Value of var is ",var)

class Child(Parent, Parent2):
    #docstring for
    def __init__(self):
        super().__init__(50)
        #self.arg = arg"""

    def altered(self):
        self.just  = 50;
        print("2.Child, BEFORE PARENT altered")
        super().altered();
        super().pri()
        super().trythis(25)
        print("3.CHILD, AFTER PARENT altered()")

#dad = Parent(75)
son = Child()

#dad.altered()
son.trythis(42)
son.altered()
print(son.__init__())
print("Final Print = ",son.just)
