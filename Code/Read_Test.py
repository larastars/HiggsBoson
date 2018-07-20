import csv
############################# READ TESTING DATA #############################
test = []
file_reader = open('test.csv', "r", encoding= "ascii")
read = csv.reader(file_reader)
for row in read:
    test.append(row)

#remove the labelling row    
test = test[1:]

"""
i = 0
while i < 5:
    print(test[i])
    print(" ")
    i +=1 
"""     

############################# LOAD A MODEL #############################
############################# CLASSIFY #############################
############################# SAVE OUTPUT ############################# 

