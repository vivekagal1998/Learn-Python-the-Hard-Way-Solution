class Parent(object):
    """docstring for ."""
    def implicit(self):
        #super(, self).__init__()
        #self.arg = arg
        print("PARENT implicit()")

class Child(Parent):
    """docstring for
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg"""
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
