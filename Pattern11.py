n = int(input("Enter the Number:"))
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=" ")
    print(" ")