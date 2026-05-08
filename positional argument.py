#DEFAULT POSITIONAL ARGUMENT 
def add(x=0,y=0,z=0):
    print(x+y+z)
add(10)

# Variable length positional argument(*args)
#b args=Variable
def display(*n):
    print(n)
    print(type(n))
display(10,20,'python',38)
display()
display(10,20)

#PACKING AMD UNPACKING 
def displays(*d): #input me * packing ka kaam karta he
    print(d)
    print(type(d))
values=eval(input("Enter all values"))
displays(*values) #output me * unpacking ka kaam karta he
