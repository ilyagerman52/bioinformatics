#!/bin/python

import random
import re

line_count = sum(1 for line in open('human_genome.fna', "r"))

random_choice = []
for i in range(125):
    random_choice.append(random.randint(0, line_count))

chosen_lines = dict()
line_now = 0
next_20 = -1
with open("human_genome.fna", "r") as genome_file:
    while True:
        line = genome_file.readline()
        if next_20 != -1:
            chosen_lines[next_20] += line[:20]
        if line_now in random_choice:
            next_20 = line_now
            chosen_lines[line_now] = line
        else:
            next_20 = -1
        line_now += 1
        if line_now == line_count:
            break
subseqs_oversampled = []
for value in chosen_lines.values():
    if bool(re.fullmatch("^[ATGCatgc\n]+$", value)):
        subseqs_oversampled.append(value)
subseqs = random.sample(subseqs_oversampled, 100)
with open("subseq_py.fasta", "w") as subseq_py_file:
    for i, seq in enumerate(subseqs):
        subseq_py_file.write(">subseq_"+str(i) + "\n")
        subseq_py_file.write(seq)
        subseq_py_file.write("\n")


#This script was tested local.