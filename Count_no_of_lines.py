#Title: Count number of line of a file
#Author: Hrishikesh H Pillai
#Date: 07-10-2020
import sys

while True:

    try:
        filename=input("Enter file name: ")
        num_lines=0
        with open(filename,"r") as f:
            for line in f:
                num_lines+=1
        print("Number of lines in file",filename,"is: ",num_lines) #Enter full path of the file
    except OSError as err:
        print("os error: {0}".format(err))
    except ValueError:
        print("\n Invalid file name\n")
    except:
        print("Unexpected error", sys.exc_info()[0])
        raise