import functools

# MAP-Transforms every element in a list by applying a function, returning a new list of the same length.
# map(function, lterable1, iterable2...)

# l1=[1,2,3,4,5]
# l2=[3,4,6,85,5]
# l3=[1,2,3,4,5]

# def sum(a,b,c):
#     return a+b+c

# # result=map(sum,l1,l2,l3) #this will only tell the address of the object 
# result=list(map(sum,l1,l2,l3))
# print(result)


# FILTER-Tests each element against a condition (predicate), returning a new list containing only elements that pass.
# filter(function, lterable)

# l=[1,2,3,4,5,6,7,8,9]
# def even(n):
#     if n%2==0:
#         return n
# res=tuple(filter(even,l))
# print(res)


# Q.1 
# input l=[1,2,3,4,4,5]
# output l=[odd,even,odd...]

# l=[1,2,3,4,4,5]
# def even_odd(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# result=tuple(map(even_odd,l))
# print(result)


# REDUCE-takes a list of items and shrinks them into one single value.

# l=[1,2,3,4,5,6]
# def add(a,b):
#     return a+b
# res=functools.reduce(add,l)
# print(res)


# max number finding  

l=[2,34,34,63,92,53,11]
def max_num(a,b):
    if a>b:
        return a
    else:
        return b

res=functools.reduce(max_num,l)
print(res)


# max number finding  

l=[2,34,34,63,92,53,11]
def min_num(a,b):
    if a<b:
        return a
    else:
        return b

res=functools.reduce(min_num,l)
print(res)

