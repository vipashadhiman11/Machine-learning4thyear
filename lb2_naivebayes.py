import csv
import random

def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

def classesInDataset(dataset):
	classes = []
	for i in range(len(dataset)):
		vector=dataset[i]
		if vector[-1] not in classes:
			classes.append(vector[-1])
	return classes


def classesInDatasetWithFreq(dataset):
	classes = {}
	for i in range(len(dataset)):
		vector=dataset[i]
		if vector[-1] not in classes:
			classes[vector[-1]]=0
		classes[vector[-1]]+=1
	return classes


def separateByClassAndCalculateFrequency(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = {}
		for j in range(len(vector)-1):
			if vector[j] not in separated[vector[-1]]: 
				separated[vector[-1]][vector[j]]=0
			separated[vector[-1]][vector[j]]+=1
	return separated


def calculateProbablity(dataset,classes,separated):
	visited={}
	cls=[]
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in visited):
			visited[vector[-1]] = []
			cls.append(vector[-1])
		for j in range(len(vector)-1):
			if vector[j] not in visited[vector[-1]]: 
				separated[vector[-1]][vector[j]]=(separated[vector[-1]][vector[j]])/float(classes[vector[-1]])
				visited[vector[-1]].append(vector[j])	
	leftFeatures=Diff(visited[cls[0]],visited[cls[1]])
	for i in range(len(leftFeatures)):
		for j in range(len(cls)):
			if leftFeatures[i] not in visited[cls[j]]:
				separated[cls[j]][leftFeatures[i]]=0.0
	return separated



def predict(model,check,classes,classesWithFrequency):
	max=0.0
	prediction='none'
	for i in range(len(classes)):
		probablity=1.0
		for j in range(len(check)):
			probablity*=model[classes[i]][check[j]]
		probablity*=classesWithFrequency[classes[i]]
		if probablity>max:
			max=probablity
			prediction=classes[i]
			print probablity
	return prediction


filename = 'train.csv'
dataset = loadCsv(filename)
trainingSet, testSet = splitDataset(dataset, 1.0)
classes=classesInDataset(dataset)
classesWithFrequency=classesInDatasetWithFreq(dataset)

#till here i have splitted my dataset into 75% and 25%. now i have to train it.

#training begins... p
# use P(H/Multiple Evidences) =  P(E1/ H)* P(E2/H) ...*P(En/H) * P(H) / P(Multiple Evidences)
# and create a table
#1	1	2596	51	3	258	0	510	221	232	148	6279	1	0	0	0	0	0	0	0	0

#we will find distinct words and use them as a rows and then we will check the classes and use them as columns. 
frequency = separateByClassAndCalculateFrequency(dataset)
print frequency
model=calculateProbablity(dataset,classesWithFrequency,frequency)
print model
#now we will test the dataset
check=raw_input().split(",")

prediction=predict(model,check,classes,classesWithFrequency)



print 'For inputs', check ,'the predicted class is ',prediction


