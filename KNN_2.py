from math import sqrt
import numpy as np

def euclidean_distance(one, two):
	distance = 0.0
	for i in range(len(one)-1):
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
		neighbors.append(int(distances[count][0][-1]))
	return neighbors

def projection(matrix):
	f = open("projection.txt", "r")
	proj =[]
	if f.mode == 'r':
		#read the file line by line 
		for line in f:
			fields = line.split(" ")
			for i in range(len(fields)):
				fields[i] = float(fields[i])
			proj.append(fields)
	proj = np.array(proj)
	matrix = np.delete(matrix, -1, 1)
	return (matrix.dot(proj))

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

		#project the pa1train
		pa1train = np.array(pa1train)
		projpa1train = projection(pa1train)		
		projpa1train = np.insert(projpa1train, 20, pa1train[:,-1], axis = 1)

		#train the training data with itself
		for test in projpa1train:
			nearest = k_neighbors(projpa1train, test, k)
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
			if predict != test[-1]:
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

		#close the file when done 
		f.close()

		#project the pa1train
		pa1train = np.array(pa1train)
		projpa1train = projection(pa1train)		
		projpa1train = np.insert(projpa1train, 20, pa1train[:,-1], axis = 1)
		pa1validate = np.array(pa1validate)
		projpa1validate = projection(pa1validate)
		projpa1validate = np.insert(projpa1validate, 20, pa1validate[:,-1], axis = 1 )

		#validate the training data with projpa1validate
		for test in projpa1validate:
			nearest = k_neighbors(projpa1train, test, k)
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
			if predict != test[-1]:
				wrong +=1

		#output the training error
		print(wrong/len(pa1validate))

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

		#close the file when done 
		f.close()

		#project the pa1train
		pa1train = np.array(pa1train)
		projpa1train = projection(pa1train)		
		projpa1train = np.insert(projpa1train, 20, pa1train[:,-1], axis = 1)
		pa1test = np.array(pa1test)
		projpa1test = projection(pa1test)
		projpa1test = np.insert(projpa1test, 20, pa1test[:,-1], axis = 1 )

		#train the training data with itself
		for test in projpa1test:
			nearest = k_neighbors(projpa1train, test, k)
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
			if predict != test[-1]:
				wrong +=1

		#output the training error
		print(wrong/len(pa1test))

print("projection test error k = 15")
testerror(15)
