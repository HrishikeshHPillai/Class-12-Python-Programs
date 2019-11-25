#Author: Hrishikesh H Pillai
#Date: 25/11/2019
#Title: Paliendrome
def pal(str):
    if len(str)<=1:
        return "Paliendrome"
    if str[0]==str[-1]:
        return pal(str[1:-1])
    else:
            return "Not Paliendrome"
while True:
    try:
        str=input("Enter String: ")
        if len(str)==0:
            print("Please Enter a Valid String")
        else:
            print(pal(str))
    except ValueError:
        print("Please Enter a Valid String")
        continue
