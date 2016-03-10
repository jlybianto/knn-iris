# ----------------
# IMPORT PACKAGES
# ----------------

from sklearn import datasets
import matplotlib.pyplot as plt

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

plt.figure()
plt.scatter(x[0:,0], x[:,1], c=y)
plt.xlabel("Sepal Length (cm)", fontsize=14)
plt.ylabel("Sepal Width (cm)", fontsize=14)
plt.title("Scatterplot of Iris Data - Sepal Length vs. Sepal Width", fontsize=16)
plt.show()

# ----------------
# MODEL DATA
# ----------------