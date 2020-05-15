n = int(input("Enter the Number:"))
for i in range(n,0,-1):
    print(" "*(i-1),end=" ")
    for j in range(i,n+1):
        print(i, end=" ")
    print(" ")