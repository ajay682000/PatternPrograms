def letter(n):
    for m in range(1):
        for i in range(n):
            for j in range((n //2 )+1):
                if((j == 0 or j == n // 2) and i != 0 or i == 0 and 
                j != 0 and j != n //2 or i == n //2):
                    print("*",end=" ")
                else:
                     print(" ", end=" ")
            print(" ")
        print("\t")
         
        
        for a in range(n):
            for b in range(n-2):
                if(b==2 or (a==0 and b!=2) or (a==6 and b<2)):
                    print("* ",end="")
                else:
                    print(end="  ")
            print()

        for i in range(n):
            for j in range((n //2 )+1):
                if((j == 0 or j == n // 2) and i != 0 or i == 0 and 
                j != 0 and j != n //2 or i == n //2):
                    print("*",end=" ")
                else:
                    print(" ", end=" ")
            print()

        for y in range(n):
            for z in range(n+1):
                if(((z==1 or z==5) and y < 2) or y==z and z >0 and z<4 or
                (z==4 and y==2)or ((z==3) and y>3)):
                    print("*", end=" ")
                else:
                    print(" ",end=" ")
            print()










letter(7)