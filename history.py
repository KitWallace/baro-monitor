import time
class History(object) :
    """ handle a sequence of timed values

    """
    
    def __init__(self,limit) :
        self.limit = limit
        self.log = []

    def load(self,file) :
        for line in file :
            (value,ts) = line.split(",")
            self.log.append((float(value),float(ts)))
      
    def add(self,value,file=None) :
        if value is None :
            pass
        else :
            ts = time.time()
            self.log.append((value,ts))
            if file is not None :
                file.write(str(value) + "," + str(ts) + "\n")
                file.flush()
                
    def add_timed(self,value,ts,file=None) :
        if value is None :
            pass
        else :
            self.log.append((value,ts))
            if file is not None :
                file.write(str(value) + "," + str(ts) + "\n")
                file.flush()

    def duration(self) :
        if self.log :
            return self.log[-1][1] - self.log[0][1]
        else :
            return 0

    def full(self) :
        return self.duration() >= self.limit

    def average_value(self) :
        total = 0
        for record in self.log :
           total = total + record[0]
        return total / len(self.log)
     
    def average_time(self) :
        return (self.log[-1][1] + self.log[0][1] ) / 2

    def average(self) :
        return (self.average_value(),self.average_time())

    def clear(self) :
        self.log = []

    def value_aged(self,age) :
        if self.duration() >= age :   
            i = len(self.log) - 1
            now = self.log[i][1]
            then = now - age
            while i >= 0 :
                item = self.log[i]
                if item[1] <= then :
                    return item[0]
                i = i - 1
            return None
        else :   
            return None

    def limit_value(self) :
        return self.value_aged(self.limit)
    
    def latest(self) :
        if self.log :
            return self.log[-1]
        else :
            return None
