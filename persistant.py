import pickle
import time

def get(name) :   
        file = open("obj/"+name+".pkl","r")
        return pickle.load(file)

class Persistant(object) :
   
    def __init__(self,name) :
        self.name = name
        self.ts = time.time()

   
    def put(self) :
        file = open("obj/"+self.name+".pkl","w")
        self.ts = time.time()
        pickle.dump(self,file,0)
        return self

