#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:37:03 2018

@author: larakamal
"""
import csv 

positive = []
negative = []
file_reader = open('Data/training.csv', "r", encoding= "ascii")
read = csv.reader(file_reader)

for row in read:
    #separate training and target
    if row[32] == 'b':
        negative.append(row)
    elif row[32] == 's':
        positive.append(row)
    else:
        negative.append(row)
        positive.append(row)

with open("Data/positive.csv", "w") as positive_file:
    writer = csv.writer(positive_file, delimiter=',')
    for line in positive:
        writer.writerow(line)

with open("Data/negative.csv", "w") as negative_file:
    writer = csv.writer(negative_file, delimiter=',')
    for line in negative:
        writer.writerow(line)
