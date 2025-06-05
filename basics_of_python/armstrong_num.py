num= int(input("Enter a no. to check if it is a armstrong no. or not:"))
num_length= len(str(num))
print(num_length)

while num>0:
    digit= num%10
    x= digit**num_length
    new_num+= x
    num= num//10

if(new_num==num):
    print("This no. is a armstrong no..")
else:
    print("This no. is not a armstrong no.")        


