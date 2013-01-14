import csv

def csvreader(csv_name):
    comicmap = dict()
    with open(csv_name, 'rb') as csvfile:
        comicreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in comicreader:
            comicmap[row[0]] = (row[1:])
    return comicmap

