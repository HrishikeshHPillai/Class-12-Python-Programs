#Author: Hrishikesh H Pillai
#Date: 24/11/2019
#Title: GCD of two numbers
def gcd(big,small):
    if small==0:
        return big
    return gcd(small,big%small)

# _main_
while (True):
    try:
        a=int(input("Enter First Number: "))
        b=int(input("Enter Second Number: "))
    except ValueError:
        print("Enter a valid Number")
        continue

    if a>=b:
        small=b
        big=a
    else:
        small=a
        big=b
    print(gcd(big,small))
