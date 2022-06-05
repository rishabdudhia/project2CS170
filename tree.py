from classifier import Classifier
from data import Data
from node import Node
from queue import Queue

from validator import Validator

class Tree: 

    def __init__(self, features: list, validator: Validator, alg):
        self.validator = validator
        self.features = features
        self.depth = 0
        if alg == 1:
            initial = Node([], self.features, 0, self.validator)
            self.greedyBuild(initial)
        else:
            end = Node(self.features, [], 0, self.validator)
            self.backwardsBuild(end)

    def backwardsBuild(self, node: Node):
        currAccuracy = node.evaluation
        f = []
        for j in range(len(node.currFeatures)):
            f.append(node.currFeatures[j]+1)
        print("Using all features, ie " + f.__str__() + ", accuracy is " + str(currAccuracy) + "%\n")
        while len(node.currFeatures) != 0:
            highestAccuracy = -1
            nextNode: Node = None
            for i in range(len(node.currFeatures)):
                rem = []
                for j in node.remainingFeatures:
                    rem.append(j)
                rem.append(node.currFeatures[i])
                curr = []
                for j in range(len(node.currFeatures)):
                    if j == i: continue
                    curr.append(node.currFeatures[j])
                newNode = Node(curr, rem, node, self.validator)
                f = []
                for j in range(len(newNode.currFeatures)):
                    f.append(newNode.currFeatures[j]+1)
                print("Using feature(s) " + f.__str__() + " accuracy is " + str(newNode.evaluation) + "%")
                if newNode.evaluation > highestAccuracy:
                    highestAccuracy = newNode.evaluation
                    nextNode = newNode
            print("")
            if highestAccuracy >= currAccuracy:
                f = []
                for j in range(len(nextNode.currFeatures)):
                    f.append(nextNode.currFeatures[j]+1)
                print("Feature set " + f.__str__() + " was best, accuracy is " + str(highestAccuracy) + "%\n")
                last = node
                node = nextNode
                currAccuracy = highestAccuracy
                if len(node.remainingFeatures) == 0:
                    f = []
                    for j in range(len(node.currFeatures)):
                        f.append(node.currFeatures[j]+1)
                    print("Using all features, ie " + f.__str__() + ", accuracy is " + str(node.evaluation) + "%\n")
                    if node.evaluation >= currAccuracy:
                        f = []
                        for j in range(len(node.currFeatures)):
                            f.append(node.currFeatures[j]+1)
                        print("Feature set " + f.__str__() + " was best, accuracy is " + str(node.evaluation) + "%\n")
                    else:
                        node = last
                        f = []
                        for j in range(len(node.currFeatures)):
                            f.append(node.currFeatures[j]+1)
                        print ("(Warning, selecting best feature set, " + f.__str__() + ", with accuracy " + str(node.evaluation) + "%" + " will decrease accuracy from " + str(currAccuracy) + "%!)")
            else:
                f = []
                for j in range(len(nextNode.currFeatures)):
                    f.append(nextNode.currFeatures[j]+1)
                print ("(Warning, selecting best feature set, " + f.__str__() + ", with accuracy " + str(highestAccuracy) + "%" + " will decrease accuracy from " + str(currAccuracy) + "%!)")
                break
        f = []
        for j in range(len(node.currFeatures)):
            f.append(node.currFeatures[j]+1)
        print("Finished search!!! The best feature subset is " + f.__str__() + " with an accuracy of " + str(node.evaluation) + "%")

    def greedyBuild(self, node: Node):
        currAccuracy = node.evaluation
        print("Using no features, ie " + node.currFeatures.__str__() + ", accuracy is " + str(currAccuracy) + "%\n")
        while len(node.remainingFeatures) != 0:
            highestAccuracy = -1
            nextNode: Node = None
            for i in range(len(node.remainingFeatures)):
                curr = []
                for j in node.currFeatures:
                    curr.append(j)
                curr.append(node.remainingFeatures[i])
                rem = []
                for j in range(len(node.remainingFeatures)):
                    if j == i: continue
                    rem.append(node.remainingFeatures[j])
                newNode = Node(curr, rem, node, self.validator)
                f = []
                for j in range(len(newNode.currFeatures)):
                    f.append(newNode.currFeatures[j]+1)
                print("Using feature(s) " + f.__str__() + " accuracy is " + str(newNode.evaluation) + "%")
                if newNode.evaluation > highestAccuracy:
                    highestAccuracy = newNode.evaluation
                    nextNode = newNode
            print("")
            if highestAccuracy >= currAccuracy:
                f = []
                for j in range(len(nextNode.currFeatures)):
                    f.append(nextNode.currFeatures[j]+1)
                print("Feature set " + f.__str__() + " was best, accuracy is " + str(highestAccuracy) + "%\n")
                last = node
                node = nextNode
                currAccuracy = highestAccuracy
                if len(node.remainingFeatures) == 0:
                    f = []
                    for j in range(len(node.currFeatures)):
                        f.append(node.currFeatures[j]+1)
                    print("Using all features, ie " + f.__str__() + ", accuracy is " + str(node.evaluation) + "%\n")
                    if node.evaluation >= currAccuracy:
                        f = []
                        for j in range(len(node.currFeatures)):
                            f.append(node.currFeatures[j]+1)
                        print("Feature set " + f.__str__() + " was best, accuracy is " + str(node.evaluation) + "%\n")
                    else:
                        node = last
                        f = []
                        for j in range(len(node.currFeatures)):
                            f.append(node.currFeatures[j]+1)
                        print ("(Warning, selecting best feature set, " + f.__str__() + ", with accuracy " + str(node.evaluation) + "%" + " will decrease accuracy from " + str(currAccuracy) + "%!)")
            else:
                f = []
                for j in range(len(nextNode.currFeatures)):
                    f.append(nextNode.currFeatures[j]+1)
                print ("(Warning, selecting best feature set, " + f.__str__() + ", with accuracy " + str(highestAccuracy) + "%" + " will decrease accuracy from " + str(currAccuracy) + "%!)")
                break
        f = []
        for j in range(len(node.currFeatures)):
            f.append(node.currFeatures[j]+1)
        print("Finished search!!! The best feature subset is " + f.__str__() + " with an accuracy of " + str(node.evaluation) + "%")



    def printTree(self):
        levels = []
        for i in range(self.depth+1):
            levels.append([])
        for i in self.tree:
            levels[i.depth].append(i)
        k = 0
        for i in levels:
            print ("depth: " + str(k) + "\n")
            for j in i: 
                print("node")
                print ("    f: " + j.currFeatures.__str__())
                print ("    r: " + j.remainingFeatures.__str__())
                for a in j.parent:
                    print("    p: " + a.currFeatures.__str__())
                    for b in a.children:
                        print("        pc: " + b.currFeatures.__str__())
                for a in j.children:
                    print("    c: " + a.currFeatures.__str__())
                    for b in a.parent:
                        print("        cp: " + b.currFeatures.__str__())

            k += 1