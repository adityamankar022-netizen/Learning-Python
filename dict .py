# Dictionary

# mutable in nature
# collection of "key" : "value"


# d={
# 'name':'person',
# 'age':37,
# 'quality':'Bhopal'
# }

# print(d)
# print(type(d))
# print(len(d))
# print(max(d))
# print(min(d))
# print(d)

# Dict Methods

# copy() create new object
# clear() remove all pairs from dict
# get() d.get('key') --> 'value'
# keys() 
# values()
# items()
# fromkeys()
# update()
# setdefault()
# pop()

# d = eval(input("Enter any dict: "))
# d1=d.copy()
# print(d)
# print(d1)
# print(id(d),id(d1))
# d.clear()
# print(d)
# x = d1.get('name')
# print(x)
# print(d1.keys())
# print(d1.values())
# print(d1.items())


#To Del the specific key
# d.pop('name')
# print(d)

#To Del the last item
# d.popitem()
# print(d)

# l=['python','java','cyber']# IN THIS THE SPECIFIC STRING WILL BECOME KEYS
# s='python'# IN THIS THE SPECIFIC ELEMENT WILL BECOME KEYS
# d=dict().fromkeys(l)
# print(d)

#UPDATE
#THIS IS USE TO UPDATE OR MERGE 2 DICTIONARY
# p={'name':'adi','age':12}
# q={'class':'bca'}
# p.update(q)
# print(p)

#SETDEFAULT
#IF THE PASSED KEY VALUE PAIR IS AVAILABLE IN THE DICT THEN THERE WILL BE NO CHANGE , IF ABSENT THEN KEY VALUE PAIR WILL BE ADDED
p={'name':'adi','age':12}
p.setdefault('name1','java')
print(p)