import csv

############################# READ TRAINING DATA #############################
training = []
#read target of training data 
target = []
file_reader = open('training.csv', "r", encoding= "ascii")
read = csv.reader(file_reader)
for row in read:
    #separate training and target
    target.append(row[-1])
    training.append(row[:-1])

#remove the labelling row    
training = training[1:]
target = target[1:]             

"""
i = 0
while i < 5:
    print(training[i])
    print(target[i])
    print(" ")
    i +=1 
        
"""        
############################# PREPROCESS DATA #############################
#columns (features) to be removed
# 1- column 1 : EventId
# 2- column 2 : 
############################# CREATE A MODEL #############################
############################# SAVE MODEL #############################
