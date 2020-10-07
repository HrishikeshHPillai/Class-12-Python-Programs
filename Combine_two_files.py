#Title: Combine two files
#Author: Hrishikesh H Pillai
#Date: 07-10-2020

import sys

while True:
    try:
        filename1=input("Enter name of file of which data has to be merged: ") #Enter full path of the file
        filename2=input("Enter name of file to which data has to be merged: ") #Enter full path of the file
        with open(filename1) as fh1, open(filename2) as fh2:
            for line1,line2 in zip(fh1,fh2):
                print(line1.rstrip("\n"),line2)
    except OSError as err:
        print("os error: {0}".format(err))
    except ValueError:
        print("\n Invalid file name\n")
    except:
        print("Unexpected error", sys.exc_info()[0])
        raise