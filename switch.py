from persistant import *

class Switch(Persistant) :
     
    def __init__(self,name) :
        self.name = name
        self.on = True
    
    def switch_on(self) :
        self.on= True
        return self

    def switch_off(self) :
        self.on= False
        return self
    
    def toggle(self) :
        self.on = not self.on
        return self

    def status(self) :
        if self.on is None :
            return "unset"
        elif self.on :
            return "on"
        else : 
            return "off"
        

                   
    
    
