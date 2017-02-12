# Under Apache 2.0 license
# Copyright - David García Pérez 2017

import csv

def parse_monthly_file(file):
    """
    It parsers a Getty monthly txt file report and returns the information as
    a dictionary, using the first line as keys
    """

    rows = []
    with open(file, mode='r') as tsv:
        for row in csv.DictReader(tsv, dialect="excel-tab"):
            rows.append(row)

    return rows
