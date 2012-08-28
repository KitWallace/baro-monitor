import pickle

def load(name) :
   
   file = open("obj/"+name+".pkl","r")
   return pickle.load(file)
   

def save(obj,name) :
   file = open("obj/"+name+".pkl","w")
   pickle.dump(obj,file,1)
   return obj

