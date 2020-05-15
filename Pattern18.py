n = int(input("Enter the Number:"))
for i in range(1,n+1):
    if(i%2==1):
        print(i, end=" ")
    else:
        print("* ", end=" ")
print(" ")
for j in range(1,n+1):
    if(j%2==0):
        print(j, end=" ")
    else:
        print("* ",end=" ")
print(" ")
for k in range(1,n+1):
    if(k%2==1):
        print("* ",end=" ")
    else:
        print(k*k,end=" ")