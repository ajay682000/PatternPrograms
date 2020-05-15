letter = input()
letter_rev = letter[::-1]
i = 0
for value in letter_rev:
    num = ord(value) - 96
    num+=i
    i+=1
    print(num, end = "")
print("\n")




