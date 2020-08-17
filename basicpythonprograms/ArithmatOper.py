class cacl:
    def __init__(self, val1, val2):
        self.val1 = val1;
        self.val2 = val2;

    def addition(self):
        c = self.val1+self.val2;
        return c;
    def subtract(self):
        c = self.val1-self.val2;
        return c;
    def multiply(self):
        c = self.val1*self.val2;
        return c;
    def divide(self):
        c = self.val1/self.val2;
        return c;

class fun(cacl):

    ins = cacl(4,2)

    print(ins.addition());
    print(ins.subtract());
    print(ins.multiply());
    print(ins.divide());

