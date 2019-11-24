#Author: Hrishikesh H Pillai
#Date: 24/11/2019
#Title: Sum of Elements of a List (Recursion)
def sum_of_list(list):
    if len(list)==0:
        return 0
    else:
        return list[0]+sum_of_list(list[1:])
while True:
    try:
        a=eval(input("Enter the list: "))
    except SyntaxError:
        print("Please enter a valid input: ")
        continue
    print(sum_of_list(a))
