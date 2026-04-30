# Calculator (Addition)

while True:
    print("1.ADDITION \n 2.SUBSTRCTION \n 3.MULTIPLE \n 4.DIVISION \n 5.OFF \n")
    n=int(input("Enter above mention any option:"))
    if n==1 or n==2 or n==3 or n==4 or n==5:
        num=[1,2,3,4,5]
    if n in num:
        if n==1:
            x=int(input("Enter how many no you want to add"))
            sum=0
            for i in range(1,x+1):
                number=int(input(f'enter {i} number:'))
                sum=sum+number
            print("Addition Answer is:",sum)
    else:
        print("Plz enter valid option")