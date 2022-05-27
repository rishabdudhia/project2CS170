from tree import Tree

print ("Welcome to Rishab Dudhia's Feature Search Algorithm\n")
print ("Please enter the total number of features: ")
numFeatures = input()
print("\nType the number of the algorithm you wish to run:")
print("1. Forward Selection")
print("2. Backwards Elimination")
alg = int(input())

features = []
for i in range(int(numFeatures)):
    features.append(i + 1)
tree = Tree(features)
# tree.printTree()
tree.solve(alg)
