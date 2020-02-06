class shape():
    def area(self):
        ar=0
        print("area of the square is: ",ar,"by default")
class square():
    def _init_(self,length):
        a=length**2
        print("area of the shape is: ",a)
c=shape()
d=square()
c.area()
d._init_(5)

