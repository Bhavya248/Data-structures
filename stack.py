#implementing a stack

class StackError(Exception):
    pass

class stack:
    top = 0
    items = []

    def length(self):
        return len(self.items)
    
    def isEmpty(self):
        if(self.top == 0):
            return True
        else:
            return False
        
    def push(self,x):
        self.items.append(x)
        self.top += 1
        
    def pop(self):
        try:
            if (self.isEmpty() == False):
                _temp = self.items[-1]
                self.items.pop()
                self.top -= 1
                return _temp
            else:
                raise StackError
        except StackError:
            print("Stack UnderFlow : Stack Has No Elements TO PoP")

    def getItem(self,index):
        try:
            if (index <= self.top - 1):
                return self.items[index]
            else :
                raise IndexError
        except IndexError:
            print("Index Out Of Range")





        
