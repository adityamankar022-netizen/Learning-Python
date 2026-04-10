# SET
# -> collection of unique element
# -> enclosed with {} and comma (,) seperated element
# -> unordered collection
# -> indexing not supported
# -> slicing not supported
# -> mutable in nature 


#Example
s={1,2,3,4,5}
e={4,5,6,7,8}
f={1,2,3,4,5,6}

#Python Inbuild funtions for set

# print(type(s))
# print(len(s))
# print(id(s))
# print(max(s)) #Error!!
# print(min(s)) #Error!!
# print(sum(s)) #Error!!

#SET METHODS

print(s.union(e)) #Union of two sets
print(s.intersection(e)) #Intersection of two sets
print(s.difference(e)) #Difference of two sets
print(s.symmetric_difference(e)) #Symmetric difference of two sets
s.intersection_update(e) #Update the set with the intersection of itself and another
print(s)
print(e)