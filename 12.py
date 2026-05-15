import functools

# LAMBDA
# nameless functions in python
# it does not require the use of return keyword
# syntax 
# lambda variable : single line exporesion

# example
# # single line addition function
# x = lambda a,b:a+b
# print(x(5,10))

# # single line square function
# sqr=lambda a:a**2
# print(sqr(5))



# MAP + LAMBDA

# single line square function using MAP and LAMBDA
# l1=[2,2,3,4,5,6,6]
# res=list(map(lambda a:a**2,l1))
# print(res)


# ++++++++++++++++++++++++++++++++++++++++fixx thiss+++++++++++++++++++++++++++++++++++++
# x=print(input("enter times of loop"))
# for i in range(x):
#     y=print(input("enter number of list"))
#     l=[]
#     for i in range(l,y+i):
#     yes=eval(input(f'enter'))
#      l.append(yes)



# FILTER + LAMBDA

l=[1,2,3,4,5]
res=list(filter(lambda n:n%2==0,l))
print(res)

res=list(filter(lambda n:n if n%2==0 else None,l))
print(res)





# RETURN + LAMBDA

# largest number in list

l=[1,2,3,4,5]
res=functools.reduce(lambda x,y:x if x>y else y,l)
print(res)
