import pandas as pd
import os
import menus
import main_header


def read_memento_mori():
    df = pd.read_csv('memento_mori.csv')
    return df


def add_record(date, dow, time, record):
    mm_df = read_memento_mori()
    columns = ['Date','Time_UTC','Day_of_Week','Record']

    record_data = {columns[0]:date, columns[1]:time, columns[2]:dow, columns[3]:record}
    mm_df = mm_df.append(record_data, ignore_index=True)
    print('\nNew record loaded into dataframe...\n')

    return mm_df


def verify_record(record):
    response = input(f'\nDo you want to add this record to Memento Mori?\n\n\"{record}\"\n\n(y/n) +> ').lower()
    return response


def new_record(date, dow, time):
    os.system('clear')
    main_header.dtg_header(date, dow, time)

    print('\nWhat would you like to record today?\n')
    record = input('+> ')

    response = verify_record(record)
    if response == 'y':
        mm_df = add_record(date, dow, time, record)
        return mm_df


def save_record(df):
    print('\nWould you like to save the record? (y/n)')
    response = input('+> ').lower()
    if response == 'y':
        df.to_csv('memento_mori.csv', index=False)
