import csv

def csv_reader():
    csvfile = open('data/data-text.csv','r')
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)

def main():
    csv_reader()

if __name__ == "__main__":
    main()