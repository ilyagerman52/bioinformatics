#!/bin/python

import sys

file_in = sys.argv[1]
file_out = "ebi.ac.uk/" + file_in

with open(file_in, 'r') as file1:
    with open(file_out, 'w') as file2:
        file2.write(">" + file1.read().split(">")[1])

