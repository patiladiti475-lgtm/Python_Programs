no = 11                           #global variable

def Display():
   global no  
   no = 21
   print("from dispkay :", no)
   
print("before :", no)
Display()
print("after :", no)
