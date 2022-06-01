from operator import ne
from tree import Tree
from data import Data
from classifier import Classifier
from validator import Validator
print ("Welcome to Rishab Dudhia's Feature Search Algorithm")
print ("Type in the name of the file to test: ")
file = input()
data = Data(file)
features = []
for i in range(data.numFeatures):
    features.append(i)
# print(features)
# print("\nType the number of the algorithm you wish to run:")
# print("1. Forward Selection")
# print("2. Backwards Elimination")
# alg = int(input())

nearestNeighbor = Classifier(data)
validator = Validator(nearestNeighbor, data)
accuracy = validator.validate([0, 14, 26])
print(accuracy)
# tree = Tree(features, validator)


# tree.printTree()
# tree.solve(alg)
