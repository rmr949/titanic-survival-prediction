import csv as csv
import numpy as np
from sklearn.naive_bayes import MultinomialNB

csv_file_object = csv.reader(open('../../data/train-modified.csv', 'rb')) #Load in the csv file
header = csv_file_object.next() #Skip the fist line as it is a header

test_features = []
train_features = []
train_values = []
temp = []

maxage = 80.0
maxsibsp = 8.0
maxparch = 9.0

for row in csv_file_object:
	temp=[]
	train_values.append(row[1])
	temp.append(float(row[2])/3)
	if row[4] is "male" :
		temp.append(0)
	else :
		temp.append(1)
	temp.append(float(row[5])/maxage)
	temp.append(float(row[6])/maxsibsp)
	temp.append(float(row[7])/maxparch)
	if row[11] == 'S' :
		temp.append(0.33)
	elif row[11] == 'Q' :
		temp.append(0.67)
	else :
		temp.append(0.99)
	train_features.append(temp)

csv_file_object = csv.reader(open('../../data/test.csv', 'rb')) #Load in the csv file
header = csv_file_object.next() #Skip the fist line as it is a header

for row in csv_file_object:
	temp=[]
	temp.append(float(row[1])/3)
	if row[3] is "male" :
		temp.append(0)
	else :
		temp.append(1)
	temp.append(float(row[4])/maxage)
	temp.append(float(row[5])/maxsibsp)
	temp.append(float(row[6])/maxparch)
	if row[10] == 'S' :
		temp.append(0.33)
	elif row[10] == 'Q' :
		temp.append(0.67)
	else :
		temp.append(0.99)
	test_features.append(temp)

gnb = MultinomialNB()
res = gnb.fit(train_features, train_values).predict(train_features)

csv_file_object = csv.reader(open('../../data/train-modified.csv', 'rb')) #Load in the csv file
header = csv_file_object.next()

predictions_file = csv.writer(open("../../results/nb-v1.csv", "wb"))
predictions_file.writerow(["PassengerId", "Survived"])

i=0
correct_count=0

for row in csv_file_object :
	predictions_file.writerow([row[0],res[i]])
	print "res[i] = "+str(res[i])+"row[i] = "+str(row[1])
	if res[i] == row[1] :
		correct_count = correct_count + 1
	i=i+1

print i

print "------------------------------------------------"
print correct_count
print "Accuracy : "+str(float(correct_count)/i)
print "------------------------------------------------"