n = int(input("Enter the Number:"))
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(i,n+1):
        print(j, end=" ")
    print(" ")