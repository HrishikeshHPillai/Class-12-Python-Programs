#Author: Hrishikesh H Pillai
#Date: 24/11/2019
#Title: Fibonacci   Number
def fibo(n):
    if n==1:
        return 0
    elif n==2:
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
    for i in range(1,a+1):
        print(fibo(i),end=", ")
    if a!=0:
        print(".....")
