import csv

def csvreader(csv_name):
    comiclist = list()
    with open(csv_name, 'rb') as csvfile:
        comicreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in comicreader:
            comiclist.append(row)
    return comiclist

