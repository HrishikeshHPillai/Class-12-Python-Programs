def fact(n): #Recursive function for calculating factorial
    if n<2:
        return 1
    else:
        return n*fact(n-1)
#Main program
a=int(input("Enter the number whose factorial is to be found: "))
print("Factorial of",a,"is:",fact(a))
