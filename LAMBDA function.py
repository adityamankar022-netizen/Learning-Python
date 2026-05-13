#LAMBDA FUNCTION (A NAME LESS FUNCTION CAN BE CREATED BY LAMBDA FUNCTION)

# EXAMPLE 1
x=lambda a,b:a+b
print(x(5,10))

#EXAMPLE 2
a=lambda a:print(a**2)
a(2)

#MAP + LAMBDA
l=[1,2,3,4,5]
b=list(map(lambda n:n**2,l))
print(b)