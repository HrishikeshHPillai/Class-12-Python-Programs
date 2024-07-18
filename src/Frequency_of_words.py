#Title: Frequency of words in a file
#Author: Hrishikesh H Pillai
#Date: 07-10-2020

import sys

def countx(lst,x):
    return lst.count(x)

try:
    while True:
        filename=input("Enter file name: ") #Enter full path of the file
        file=open(filename,"r")
        lines=file.read()
        wordlist=lines.split()
        word=str(input("Enter file word to be counted: "))
        frequency=countx(lines,word)
        print("Number of words in file",filename,"is: ",frequency)
except OSError as err:
    print("os error: {0}".format(err))
except ValueError:
    print("\n Invalid file name\n")
except:
    print("Unexpected error", sys.exc_info()[0])
    raise