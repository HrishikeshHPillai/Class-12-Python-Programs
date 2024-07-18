#title:Menu driven python program with functions to push and pop stack elements in a stack for a book details
#Author:Hrishikesh H Pillai
#Date:10-11-2019

#Functions
def isEmpty(stk): #Function to check if the stack is empty
    if stk==[]:
        return True
    else:
        return False

def push(stk,item): #Fuction to push the data into the stack
    stk.append(item)
    top=len(stk)-1

def pop(stk): #Function to pop the data from the stack
    if isEmpty(stk):
        print("Stack is empty")
    else:
        item=stk.pop()
    if len(stk)==0:
        top=None
    else:
        print("\nBook No\t Book Name\n")
        top=len(stk)-1
    print(item[0],"\t",item[1],"\n")

def peek(stk):#Function to display the item in the top of the stack
    if isEmpty(stk):
        print("Stack is empty")
    else:
        top=len(stk)-1
        print("\nBook No\t Book Name\n")
        item=stk[top]
        print(item[0],"\t",item[1],"\n")

def disp(stk):#Function to display all the items in the stack
    if isEmpty(stk):
        print("Stack is empty")
    else:
        top=len(stk)-1
        print("\nBook No\t Book Name\n")
        for i in range(top,-1,-1):
            item=stk[i]
            print(item[0],"\t",item[1],"\n")

#Main program
stack=[]
top=None
while True:
    try:
        func=int(input("\n*****************************************\nChoose one stack operation:\n\n\t 1.Push\n\t 2.Pop\n\t 3.Peek\n\t 4. Display\n\t 5. Quit\n\n*****************************************\n\nYour Choice: ")) #To choose from one of the operations on stack
    except ValueError:
        print("Plese enter a valid input")
        continue
    if func==1:
        item=[]
        try:
            bookno=int(input("Enter Book Number: "))
        except ValueError:
            print("Enter a valid Book Number")
            continue
        try:
            bookname=str(input("Enter Book Name: "))
        except ValueError:
            print("Enter a valid Book Name")
            continue
        item.append(bookno)
        item.append(bookname)
        push(stack,item)
    elif func==2:
        pop(stack)
    elif func==3:
        peek(stack)
    elif func==4:
        disp(stack)
    elif func==5:
        print("\n**************************************************\n")
        print("Thankyou for using the stack operation program.\nFrom the developer Hrishikesh H Pillai")
        print("\n**************************************************\n")
        break
    else:
        print("Please enter a valid input")
