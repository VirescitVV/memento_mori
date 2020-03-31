import pandas as pd
import os
import record_mgmt

#my main menu function
#consider rolling other menus from, say, record_mgmt.py into this as functions
def main_menu(date, dow, time):
    print(' -----------------------------------------------------------------')
    print('1] Add new record | 2] Display record | 3] Delete record | 4] Exit\n')
    choice = input('+> ')
    #creates new record and saves it
    if choice == '1':
        df = record_mgmt.new_record(date, dow, time)
        record_mgmt.save_record(df)
        return True
    #exits the program after clearing the screen
    elif choice == '4':
        os.system('clear')
        return False
    #all others loop back to main screen
    else:
        return True
