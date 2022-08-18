import sqlite3 as sql
import requests as req

# User defined class imports
import Link

'''
Main thread that handles setup and start of main program
'''
if __name__ == '__main__':
    __isRunning = True
    __curInput = ""
    while __isRunning:
        __curInput = input("Input a link to check\n")

        print("Testing "+str(__curInput))
        __curReq = req.get(str(__curInput))
        print(str(__curReq))
        __curInput = input("Enter Q to quit, any other key will continue\n")

        if(__curInput == "Q" or __curInput == "q"):
            __isRunning = False
