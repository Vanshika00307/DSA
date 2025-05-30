num= int(input("enter a no.= "))
reverse_no=0

while num>0:
    digit= num%10
    reverse_no=reverse_no*10 + digit
    num=num//10


   

print("The reverse of no.",num,"is",reverse_no)    
