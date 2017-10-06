class Just(object):
    """docstring for ."""
    def __init__(self, arg):
        #super(, self).__init__()
        self.arg = arg

    def playme(self):
        for key,value in self.arg.items():
            print("Key is %s and Value is %s"%(key,value))


obj = Just({'name': 'Vivek Shah',
            'age': 15,
            'height': 25})

obj.playme()
