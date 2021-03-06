# ----------------
# IMPORT PACKAGES
# ----------------

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# ----------------
# OBTAIN DATA
# ----------------

iris = datasets.load_iris()

# ----------------
# PROFILE DATA
# ----------------

observations = len(iris.data)
features = len(iris.feature_names)
print("Number of Observations: " + str(observations))
print("Number of Features: " + str(features))
print("")

print("Features: ")
for i in iris.feature_names:
	print i
print("")

x = iris.data[0:,:2] # Filter just the first two columns (sepal length and sepal width)
y = iris.target

# ----------------
# VISUALIZE DATA
# ----------------

# Scatterplot of sepal length against sepal width colored by different types.
plt.figure()
plt.scatter(x[0:,0], x[:,1], c=y)
plt.xlabel("Sepal Length (cm)", fontsize=14)
plt.ylabel("Sepal Width (cm)", fontsize=14)
plt.title("Scatterplot of Iris Data - Sepal Length vs. Sepal Width", fontsize=16)
plt.savefig("sepal-scatterplot.png")

# ----------------
# MODEL DATA
# ----------------

# Generation for a new data point
length = []
for i in enumerate(x):
	length.append(i[1][0])

width = []
for j in enumerate(x):
	width.append(j[1][1])

point = []
point.append(np.random.uniform(min(length), max(length)))
point.append(np.random.uniform(min(width), max(width)))
print("Classification Test from Randomized Point: ")
print("Random Generated Point: " + str(point))
print("Selected Number of Nearest Neighbors (k): 10")

# Calculation of two-dimensional Euclidean distance from generated data point to exisiting points
distance = [] # Empty list to contain distance and target coordinates
count = 0 # Count to assign type of target from iris.target
for n in x:
	d = np.sqrt((n[0] - point[0]) ** 2 + (n[1] - point[1]) ** 2)
	distance.append([d, y[count]])
	count += 1

distance.sort() # Sort calculated distances in ascending order
top_ten = distance[0:10]

target = []
for i in top_ten:
	target.append(i[1])

print("Number of Seritosa Species: " + str(Counter(target)[0]))
print("Number of Verisicolor Species: " + str(Counter(target)[1]))
print("Number of Virginica Species: " + str(Counter(target)[2]))

species = ""

if Counter(target)[0] > Counter(target)[1] and Counter(target)[0] > Counter(target)[2]:
   	species = "Seritosa"
elif Counter(target)[1] > Counter(target)[0] and Counter(target)[1] > Counter(target)[2]:
   	species = "Versicolor"
elif Counter(target)[2] > Counter(target)[0] and Counter(target)[2] > Counter(target)[1]:
	species = "Virginica"
else:
	species = "Species cannot be determined"

print("Classification of Generated Data Point: " + str(species))
print("")

# ----------------
# USER INPUT
# ----------------

print("Classification Test for an Arbitrary User Input Point: ")

# Define a function that takes in arbitrary user inputs and determine species through model.
def knn(user_length, user_width, user_k):
	iris = datasets.load_iris()
	x = iris.data[:,:2]
	y = iris.target

	distance = []
	count = 0

	for n in x:
		d = np.sqrt((n[0] - user_length) ** 2 + (n[1] - user_width) ** 2)
		distance.append([d, y[count]])
		count += 1

	distance.sort() # Sort calculated distances in ascending order
	top_k = distance[0:user_k]

	target = []
	for i in top_k:
		target.append(i[1])

	print("Number of Seritosa Species: " + str(Counter(target)[0]))
	print("Number of Verisicolor Species: " + str(Counter(target)[1]))
	print("Number of Virginica Species: " + str(Counter(target)[2]))

	species = ""

	if Counter(target)[0] > Counter(target)[1] and Counter(target)[0] > Counter(target)[2]:
   		species = "Seritosa"
	elif Counter(target)[1] > Counter(target)[0] and Counter(target)[1] > Counter(target)[2]:
   		species = "Versicolor"
	elif Counter(target)[2] > Counter(target)[0] and Counter(target)[2] > Counter(target)[1]:
		species = "Virginica"
	else:
		species = "Species cannot be determined"

	print("Classification of Arbitrary Input: " + str(species))

# Allow user to input arbitrary sepal length and sepal width for the model to make a prediction.
user_length = float(raw_input("Input a sepal length (3.00 - 9.00 cm): "))
user_width = float(raw_input("Input a sepal width (1.00 - 5.00 cm): "))
user_k = int(raw_input("Input an integer (k) for number of nearest neighbors: "))
knn(user_length, user_width, user_k)