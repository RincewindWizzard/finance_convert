#!/usr/bin/python3
import sys
import csv
from datetime import date, datetime
from collections import namedtuple



Transaktion = namedtuple('Transaktion', [
    'date',
    'description',
    'amount'
])
def import_csv(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            row = list(cell.replace('\n', ' ') for cell in row)
            buchung = Transaktion(
                datetime.strptime(row[0], '%d.%m.%Y').strftime('%Y-%m-%d'), 
                row[8].replace('Summenbeleg ', ''), 
                ('-' if row[12] == 'S' else '') + row[11])
            print('"{}","{}","{}"'.format(*buchung))

if __name__ == '__main__':
    import_csv(sys.argv[1])
    
