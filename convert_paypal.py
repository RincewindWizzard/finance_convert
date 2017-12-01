#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import csv
import codecs
from datetime import date, datetime
from collections import namedtuple

Transaktion = namedtuple('Transaktion', [
    'date',
    'description',
    'currency',
    'amount'
])
def import_csv(path):
    with codecs.open(path, 'r', encoding='latin1') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        for row in reader:
            #row = list(cell.replace('\n', ' ') for cell in row)
            buchung = Transaktion(
                datetime.strptime(row[0], '%d.%m.%Y').strftime('%Y-%m-%d'), 
                None,
                row[6],
                row[7])
            print(buchung)
            #print('"{}","{}","{}"'.format(*buchung))

if __name__ == '__main__':
    import_csv(sys.argv[1])
