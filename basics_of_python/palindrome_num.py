num= int(input("enter a no. to check whether it is a palindrome no. or not: "))

original_num=num
rev_num=0

while num>0:
    digit= num%10
    rev_num=rev_num *10+ digit
    num= num//10

if(rev_num==original_num):
    print("This no. is a palindrome no.")  
else:
    print("This no. is not a palindrome no.")
    
