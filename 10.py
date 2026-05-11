#. VARIABLES SCOPE 

#if True:
   # x=10
    #print(x)
#print(x)
'''
x=20
def add():
    global x #global keyword 
    x=10
    print(x)
add()
print(x)  '''  
    
    
x=20
def add():
    x=1500
    print(x)
    print(globals()['x']) #to access global to local
add()
print(x)    
       