#Author: Hrishikesh H Pillai
#Date: 24/11/2019
#Title: Fibonacci   Number
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
while True:
    try:
        a=int(input("Enter Number: "))
    except ValueError:
        print("Enter a valid Number")
        continue
    if a==0:
        print("Enter a positive number")
        continue
    print(fibo(a))