class A:
    def f(self):
        print("1")
        return self.g()

    def g(self):
        print("2")
        return 'A'

class B(A):
    def g(self):
        print("3")
        return 'B'

a = A()
b = B()
print (a.f())
print (b.f())
print (a.g())
print (b.g())
