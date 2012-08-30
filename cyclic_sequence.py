import time
class Cyclic_Sequence(object) :
    """ handle a circular sequence of objects

    """
    
    def __init__(self,limit) :
        self.limit = limit
        self.seq = [None for i in range(limit)]
        self.current = self.limit - 1
      
    def add(self,obj) :
        if obj is None :
            pass
        else :
            self.current = (self.current + 1) % self.limit
            self.seq[self.current] = obj

    def get(self,i) :
        index = (self.current - i ) % self.limit 
        return self.seq[index]

    def pr(self) :
        for i in range(self.limit) :
            print i,self.get(i)
