rows=int(input("Enter the value of rows:"))

for i in range(0,rows):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,rows):
        print("*",end=" ")
    print()    

