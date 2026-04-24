             # Table printing using FOR loop


#STATIC

'''for i in range(1,10):
    for j in range (1,10):
        print(j,end=' ')
    print()
'''

# # DYNAMIC

''''n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range (1,n+1):
        print(j,end=' ')
    print()
'''

# Right angle triangle

'''for i in range(1,10):
    for j in range (1,i+1):
        print(j,end=' ')
    print()
'''

# Right angle triangle (consicutive numbers)

'''n=int(input("Enter the number"))
x=1
for i in range(1,n+1):
    for j in range (1,i+1):
        print(x,end=' ')
        x=x+1
    print()
'''

# Right angle triangle (alphabets consicutive)

n=int(input("Enter the number"))

ch='A'
for i in range(1,n+1):
    for _ in range (1,i+1):
        print(ch,end=' ')
        ch=chr(ord(ch)+1)
    print()