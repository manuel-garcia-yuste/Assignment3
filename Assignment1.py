#!/usr/bin/env python

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program determines which month it is depending the number


def main():
    # this function runs the program

    # input
    integer = int(input("Enter an integer: "))

    # process
    if (integer == 1):
        print("Sunday")
    elif (integer == 2):
        print ("Monday")
    elif (integer == 3):
        print ("Tuesday")
    elif (integer == 4):
        print ("Wednesday")
    elif (integer == 5):
        print ("Thursday")
    elif (integer == 6):
        print ("Friday")
    elif (integer == 7):
        print ("Saturday")


if __name__ == "__main__":
    main()
