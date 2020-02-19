def add(*args):
    print(args)
def add(*args):
    print(args)

add(10,39,[1,2,3,4])
add(10,39,12)

class A:
    def fly(self):
        print("flying a")
class B(A):
    def fly(self):
        print("flying b")

a=B()
a.fly()
