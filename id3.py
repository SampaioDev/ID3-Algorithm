import csv
import math
import random

def calculate_entropy(num):
    print(num)
    result = math.log2(num)
    return result

def get_file():
    with open('risco.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            print(row)
            print(row[0])
            print(row[0],row[1],row[2],)

def id3():
    result = calculate_entropy(random.randint(0, 100))
    print(result)

def main():
    get_file()
    id3()

if __name__ == "__main__":
    main()