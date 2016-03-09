# ----------------
# IMPORT PACKAGES
# ----------------

from sklearn import datasets

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

# ----------------
# MODEL DATA
# ----------------