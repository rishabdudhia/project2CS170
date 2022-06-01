from tree import Tree
from data import Data
print ("Welcome to Rishab Dudhia's Feature Search Algorithm")
print ("Type in the name of the file to test: ")
file = input()
data = Data(file)
features = []
for i in range(data.numFeatures):
    features.append(i)

print("\nType the number of the algorithm you wish to run:")
print("1. Forward Selection")
print("2. Backwards Elimination")
alg = int(input())

tree = Tree(features, data)
# tree.printTree()
tree.solve(alg)
