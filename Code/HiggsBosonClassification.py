import csv

############################# READ TRAINING DATA #############################
training = []
#read target of training data 
target = []
file_reader = open('Data/training.csv', "r", encoding= "ascii")
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
# 1- column 0 : EventId
# 2- column 5 : DER_deltaeta_jet_jet
# 3- column 6 : DER_mass_jet_jet
# 4- column 7 : DER_prodeta_jet_jet
# 5- column 13 : DER_lep_eta_centrality
# 6- column 27 : PRI_jet_subleading_pt
# 7- column 28 : PRI_jet_subleading_eta
# 8- column 29 : PRI_jet_subleading_phis
# 9- column 31: weight, we cannot use it as a feature because test set doesnt have it

for row in training:
    del row[0]
    del row[5-1]
    del row[6-2]
    del row[7-3]
    del row[13-4]
    del row[27-5]
    del row[28-6]
    del row[29-7]
    del row [31-8]
    
#data is stored as string rather than float so we have to conver them
for i in range(len(training)):
    for j in range(len(training[0])):
        training[i][j] = float( training[i][j])
        
############################# CREATE A MODEL #############################
#create naive bayes model 
#http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
#steps to create naive bayes model:
# 1- import model 
from sklearn.naive_bayes import GaussianNB

# 2- look at the parameters of the model 
   # Parameters:	
   # priors : array-like, shape (n_classes,)
   # Prior probabilities of the classes. If specified the priors are not adjusted according to the data.
   # we have total of 250,000 instances, backgroud = 164,333, signal = 85,667
   # probability of background = 164,333/250,000  = 0.657
   # probability of signal = 85,667/250,000  = 0.3427

model = GaussianNB()
model.fit(training, target)

############################# READ TEST DATA #############################
test = []
file_reader = open('Data/test.csv', "r", encoding= "ascii")
read = csv.reader(file_reader)
for row in read:
    test.append(row)

#remove the labelling row    
test = test[1:]

#remove unwanted columns 
for row in test:
    del row[0]
    del row[5-1]
    del row[6-2]
    del row[7-3]
    del row[13-4]
    del row[27-5]
    del row[28-6]
    del row[29-7]
    
#convert test to float 
for i in range(len(test)):
    for j in range(len(test[0])):
        test[i][j] = float( test[i][j])
 
print(test[0])       
############################# CLASSIFY #############################
output = model.predict(test)

############################# SAVE OUTPUT ############################# 
count = 2
file = open("Data/result.txt", "w")
for i in output:
    file.write(str(count))
    file.write("\t")
    file.write(str(i))
    file.write("\n")
    count = count+1

file.close()
