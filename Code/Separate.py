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

#neg_count = 1
#pos_count = 1
for row in read:
    #separate training and target
    if row[32] == 'b':
        #row.insert(0, neg_count)
        #neg_count = neg_count + 1
        negative.append(row)
    elif row[32] == 's':
        #row.insert(0, pos_count)
        #pos_count = pos_count+1
        positive.append(row)
    else:
        #row.insert(0, "number")
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
