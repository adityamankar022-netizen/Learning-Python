# Transfer Statement


# Continue statement -> Skip current iteration 
# Example:

for i in range(5):
    if i == 5:
        continue
    print(i)
    i=i+1


# Break statement -> Terminate current loop
# Example:
'''
for i in range(5):
    if i == 2:
        break
    print(i)
    i=i+1
'''

# Pass Statement -> Skip current block
# Example:
'''
for i in range(5):
    if i == 2:
        pass
    print(i)
    i=i+1
'''