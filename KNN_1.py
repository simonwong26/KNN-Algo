#code for part 1
from math import sqrt
import numpy as np

def euclidean_distance(one, two):
	distance = 0.0
	for i in range(784):
		distance += (one[i] - two[i])**2
	return sqrt(distance)

def k_neighbors(train, test, k):
	distances = []
	for train_r in train:
		distance = euclidean_distance(train_r, test)
		distances.append((train_r, distance))
		distances.sort(key=lambda x: x[1])
	neighbors = []
	for count in range(k):
		neighbors.append(distances[count][0][784])
	return neighbors

def trainingerror(k):
	f = open("pa1train.txt", "r")
	pa1train = []
	nearest = []
	wrong = 0
	#check if the file is opened
	if f.mode == 'r':
		#read the file line by line 
		for line in f:
			fields = line.split(" ")
			fields[784] = int(fields[784][0])
			for i in range(len(fields)):
				fields[i] = int(fields[i])
			pa1train.append(fields)

		#train the training data with itself
		for test in pa1train:
			nearest = k_neighbors(pa1train, test, k)
			#print(nearest)

			#identify the labels occurs most often 
			count = [0]*10
			for x in nearest:
				count[x]+=1
			max = 0
			predict = 0
			for x in range(len(count)):
				if count[x] > max:
					max = count[x]
					predict = x

			#check if the output is correct
			if predict != test[784]:
				wrong +=1

		#output the training error
		print(wrong/len(pa1train))

	#close the file when done 
	f.close()

def validateerror(k):
	f = open("pa1train.txt", "r")
	pa1train = []
	nearest = []
	wrong = 0
	#check if the file is opened
	if f.mode == 'r':
		#read the file line by line 
		for line in f:
			fields = line.split(" ")
			fields[784] = int(fields[784][0])
			for i in range(len(fields)):
				fields[i] = int(fields[i])
			pa1train.append(fields)

	#close the file when done 
	f.close()

	#start read pa1validate
	f = open("pa1validate.txt", "r")
	pa1validate = []
	if f.mode == 'r':
		#read the file line by line 
		for line in f:
			fields = line.split(" ")
			fields[784] = int(fields[784][0])
			for i in range(len(fields)):
				fields[i] = int(fields[i])
			pa1validate.append(fields)

		#valide the training data with pa1validate
		for test in pa1validate:
			nearest = k_neighbors(pa1train, test, k)
			#print(nearest)

			#identify the labels occurs most often 
			count = [0]*10
			for x in nearest:
				count[x]+=1
			max = 0
			predict = 0
			for x in range(len(count)):
				if count[x] > max:
					max = count[x]
					predict = x

			#check if the output is correct
			if predict != test[784]:
				wrong +=1

		#output the training error
		print(wrong/len(pa1validate))

	#close the file when done 
	f.close()

def testerror(k):
	f = open("pa1train.txt", "r")
	pa1train = []
	nearest = []
	wrong = 0
	#check if the file is opened
	if f.mode == 'r':
		#read the file line by line 
		for line in f:
			fields = line.split(" ")
			fields[784] = int(fields[784][0])
			for i in range(len(fields)):
				fields[i] = int(fields[i])
			pa1train.append(fields)

	#close the file when done 
	f.close()

	#start read pa1validate
	f = open("pa1test.txt", "r")
	pa1test = []
	if f.mode == 'r':
		#read the file line by line 
		for line in f:
			fields = line.split(" ")
			fields[784] = int(fields[784][0])
			for i in range(len(fields)):
				fields[i] = int(fields[i])
			pa1test.append(fields)

		#test the training data with pa1test
		for test in pa1test:
			nearest = k_neighbors(pa1train, test, k)
			#print(nearest)

			#identify the labels occurs most often 
			count = [0]*10
			for x in nearest:
				count[x]+=1
			max = 0
			predict = 0
			for x in range(len(count)):
				if count[x] > max:
					max = count[x]
					predict = x

			#check if the output is correct
			if predict != test[784]:
				wrong +=1

		#output the training error
		print(wrong/len(pa1test))

	#close the file when done 
	f.close()

print("test error k = 1")
testerror(1)