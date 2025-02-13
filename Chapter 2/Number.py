num=int(input("Enter the number : "))
if num%5 == 0:
    if num%2==0:
        print("The is divisible by 5 and also it is even")
    else:
        print("The is divisible by 5 but it is not even")
else:
    if num%2==0:
        print("The number is not divisible by 5 but it is even")
    else:
        print("The number neither divisible by nor even")
