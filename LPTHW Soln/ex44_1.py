class Parent(object):
    """docstring for ."""
    def implicit(self):
        #super(, self).__init__()
        #self.arg = arg
        print("PARENT implicit()")

class Child(Parent):
    """docstring for
    def __init__(self, arg):"""
        #self.arg = arg
    def implicit(self):
        print("This is Child Class1")
        super(Child, self).implicit()
        print("This is CHild Class2")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
