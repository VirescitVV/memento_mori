import pandas as pd
import main_header
import get_dtg
import menus

#main function
def main():
    #retrieves system dtg for record management
    date, dow, time = get_dtg.get_dtg()
    loop = True

    #while loop to keep program looping. menus.py includes loop break conditions
    while loop:
        main_header.print_header_dtg(date, dow, time)
        loop = menus.main_menu(date, dow, time)

main()
