import csv
import sys
import collections

def __main__ ():
    input_name = 'simple_test3'
    path = './%s.csv'%input_name


    with open(path,mode='r') as inp:
        reader = csv.reader(inp)
        header = next(reader)
        dict_from_csv = {rows[1]:0 for rows in reader}
    print(dict_from_csv)
    graph_table = dict(sorted(dict_from_csv.items(), reverse=False))
    print(graph_table)
