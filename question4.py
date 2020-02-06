class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()

output:0,1 because derived test carries all the character of test as test class is parent class and derived test is child class.


class A:
    def __init__(self, x=1):
        self.x = x
class der(A):
    def __init__(self, y=2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main()

output: 1 2 because der is derived from A which have constructor inside both of them.obj is the object of
der and is also the object of A and both of them are called and is printed.

class A:
    def __init__(self, x):
        self.x = x
    def count(self, x):
        self.x = self.x + 1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()

output:3 1


class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
    def multiply(self, i):
        self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
    def multiply(self, i):
        self.i = 2 * i;
obj = B()

output:30