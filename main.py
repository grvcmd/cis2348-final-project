# Ken Valverde
# 1527936
# CIS 2348: Final Project

import sys
import csv
import operator

user_input = ''


# Get filename from user
def get_filename():
    global user_input
    while user_input != 'upload':
        try:
            filename = input("Enter filename: ")
            if ".csv" not in filename:
                raise ValueError('Please include ".csv" file extension.')


        except ValueError as excpt:
            print(excpt)
            print('Might not upload.\n')

        user_input = input("Enter any key to try again ('upload' to quit): ")
    return filename


def process_inventory(file):
    try:
        with open(file) as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            sorted_list = sorted(data, key=operator.itemgetter(1))

        with open('FullInventory.csv', 'w') as f:
            csv_writer = csv.writer(f)
            for row in sorted_list:
                csv_writer.writerow(row)


    except FileNotFoundError:
        print("Filename: '{}' not found.".format(file))


# OBJ 1: PROCESSED INVENTORY REPORTS:
# OBJ 1a. Define function to write over FullInventory.csv file with inputted csv files


# OBJ 1b. TODO: write each row in LaptopInventory.csv to their own .txt file.
# TODO: items should be sorted by their item ID
# TODO: Each item type (named after itself) have its own file.
# TODO: Each row should contain the item ID, manufacturer name, price, service date, and status


if __name__ == '__main__':
    print("Welcome to ManageManage\n")

    file = get_filename()
    process_inventory(file)
