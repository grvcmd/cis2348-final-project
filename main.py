"""

    Product inventory manager program
    Ken Valverde
    CIS 2348 Final Project

    Program functions

    - Import csv files
    - Create Inventory reports
    - Find item in the inventory

"""

import csv
import os
import operator


# Gets filename
def get_file():
    file = input("Enter filename: ")
    print("{} uploaded.\n".format(file))
    return file + '.csv'


class File:
    def __init__(self, file):
        self.file = file

    # Outputs entire file into FullInventory.csv
    def full_inventory(self):
        with open(self.file, 'r') as inputfile:
            reader = csv.reader(inputfile, delimiter=',')

            # sort filename alphabetically by manufacturer (index[1])
            sorted_list = sorted(reader, key=operator.itemgetter(1))

            # Write to FullInventory.csv
            with open('FullInventory.csv', 'w', newline='') as outfile:  # newline prevents empty lines when writing
                writer = csv.writer(outfile)
                for row in sorted_list:
                    writer.writerow(row)

    # Outputs different item types to their own files.
    def item_type(self):
        with open('FullInventory.csv', 'r') as inputfile:
            reader = csv.reader(inputfile, delimiter=',')

            # Iterate over each row
            for row in reader:
                # Iterate over column C3 only
                for column in row[2:3]:

                    # Item type: phone
                    if column == 'phone':
                        with open('PhoneInventory.csv', 'w', newline='') as output:
                            writer = csv.writer(output)
                            writer.writerow(row)
                    # Item type: laptop
                    elif column == 'laptop':
                        with open('LaptopInventory.csv', 'w', newline='') as output:
                            writer = csv.writer(output)
                            writer.writerow(row)
                    # Item type: tower
                    elif column == 'tower':
                        with open('TowerInventory.csv', 'w', newline='') as output:
                            writer = csv.writer(output)
                            writer.writerow(row)

    def find_item(self, manufacturer, item_type):
        try:
            with open('FullInventory.csv', 'r') as inputfile:
                reader = csv.reader(inputfile, delimiter=',')

                # Iterate over each row
                for row in reader:
                    # Iterate over column C3 only
                    for column in row[2:3]:
                        if item_type in column:
                            print(', '.join(row))
        except TypeError:
            print("\nNo such item in inventory.")


if __name__ == '__main__':
    user = File(get_file())
    user.full_inventory()
    user.item_type()

    print("Searching for an item?")
    manufacturer = input("Enter manufacturer: ")
    item_type = input("Enter item type: ")
    print('\n')
    user.find_item(manufacturer, item_type)