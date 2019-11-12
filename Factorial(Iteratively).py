n=int(input("Enter the number whose factorial is to be found: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of",n,"is:",fact)
