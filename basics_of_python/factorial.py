def find_factorial(num):
    if num<0:
        print("Factorial is not defined for negative numbers.")

    factorial=1

    for i in  range(1,num+1):
        factorial*=i
    return factorial

num=int(input("Enter a no., for finding its factorial:"))
result = find_factorial(num)
print("The factorail of number",num,"is =",result)



 