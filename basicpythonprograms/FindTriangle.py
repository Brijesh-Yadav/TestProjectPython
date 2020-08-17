class tri:
    def __init__(self, a, b):
        self.a = a;
        self.b = b;

    def display(self):
        print(self.a,self.b)

class implement (tri):
    cl = tri(3,4)
    cl.display();
