import time
class CBuffer(object) :
    """ handle a circular sequence values

    """
    
    def __init__(self,limit) :
        self.limit = limit
        self.log = [None for i in range(limit)]
        self.i = self.limit - 1

    def load(self,file) :
        for line in file :
            (value,ts) = line.split(",")
            self.log.append((float(value),float(ts)))
      
    def add(self,value) :
        if value is None :
            pass
        else :
            self.i = (self.i + 1) % self.limit
            self.log[self.i] = value

    def value(self,age) :
        index = (self.i - age) % self.limit 
        return self.log[index]

    def pr(self) :
        for i in range(self.limit) :
            print i,self.value(i)
