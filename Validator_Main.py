import sqlite3 as sql
import requests as req

# User defined class imports
import link as lin

'''
Main thread that handles setup and start of main program
'''
if __name__ == '__main__':
    __is_running = True
    __cur_input = ""
    
    while __is_running:
        __cur_input = input("Input a link to check\n")
        r = lin.Link(str(__cur_input))

        # Make request for given link    
        try:
            print("Testing "+r.link)
            r.status = req.get(r.link)
            print(r.status)
        except:
            print("Invalid link")

        # Determine if user wants to continue or quit
        __cur_input = input("Enter Q to quit, any other key will continue\n")

        if(__cur_input == "Q" or __cur_input == "q"):
            __is_running = False
