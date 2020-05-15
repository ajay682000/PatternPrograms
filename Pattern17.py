n = int(input("Enter the Number:"))
for i in range(1,n+1):
    if(i%3==0):
        print("# ", end=" ")
    elif(i%3==2):
        print("$ ",end=" ")
    else:
        print("* ", end=" ")