# Ken Valverde
# 1527936
# CIS 2348: Final Project

import csv
import operator


user_input = ''

# Get filename from user
def get_file():
    global user_input
    while user_input != 'upload':
        try:
            filename = input("Enter filename: ")
            if ".csv" not in filename:
                raise ValueError('Please include ".csv" file extension.')

        except ValueError as excpt:
            print(excpt)
            print('Could not upload.\n')

        user_input = input("Enter any key to try again ('upload' to quit): ")
    return filename


# OBJ 1: Processed Inventory Reports:

# OBJ 1a. Define function to print FullInventory.csv
def print_inventory():
    try:
        # Read FullInventory.csv
        with open(get_file(), 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')

            # Print in this order >>> item ID, Manufacturer name, Item type, Service date, Status
            print('\n')
            print("{:<12} {:<15} {:<14} {:<10} {:<17} {:<15}".format('Item ID', 'Manufacturer', 'Item type', 'Price',
                                                                     'Service Date', 'Status'))
            for eachrow in csv_reader:
                print("{:<12} {:<15} {:<14} {:<10} {:<17} {:<15}".format(*eachrow))
    except FileNotFoundError:
        print("File not found.")


# OBJ 1b. TODO: write each row in LaptopInventory.csv to their own .txt file.
# TODO: items should be sorted by their item ID
# TODO: Each item type (named after itself) have its own file.
# TODO: Each row should contain the item ID, manufacturer name, price, service date, and status


if __name__ == '__main__':
    print_inventory()
