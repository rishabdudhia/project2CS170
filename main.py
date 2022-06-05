from tree import Tree
from data import Data
from classifier import Classifier
from validator import Validator
import time

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
# accuracy = validator.validate([0, 14, 26])
# print(accuracy)
print("Please enter the algorithm you would like to run:")
print("1. Forward Selection")
print("2. Backwards Elimination")

alg = 0
while alg == 0:
    alg = input()
    if alg == '1':
        alg = int(alg)
    elif alg == '2':
        alg = int(alg)
    else:
        print("Sorry please select between options 1 and 2")
        alg = 0
test = [0,1,2,3,4,5,6,7,8,9]
before = time.perf_counter()
tree = Tree(features, validator, alg)
after = time.perf_counter()
difference = after - before
print("")

print("Algorithm execution took: %.4f seconds." % difference)