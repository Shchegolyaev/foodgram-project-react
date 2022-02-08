


class A():
    def m(self):
        print("A")

class B():
    def m(self):
        print("B")

class C(A, B):
    def m(self):
        super().m()
        print("C")

C().m()