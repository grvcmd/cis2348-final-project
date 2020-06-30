import csv
import pandas as pd
import operator


# User-input file class
class InputFile:
    # Params: name of file
    def __init__(self, filename):
        self.filename = filename

    # Define get_file function
    def get_file(self):

        # Read csv file
        with open(self.filename, 'r') as infile:
            reader = csv.reader(infile, delimiter=',')

            # Sort self.filename alphabetically by Manufacturer (index[1] of each row)
            sorted_list = sorted(reader, key=operator.itemgetter(1))

            # Write everything we read from self.filename to FullInventory.csv
            with open('FullInventory.csv', 'w') as outfile:
                writer = csv.writer(outfile)
                for row in sorted_list:
                    writer.writerow(row)


if __name__ == '__main__':

    filename = input("Enter filename: ")
    user = InputFile(filename)
    user.get_file()


