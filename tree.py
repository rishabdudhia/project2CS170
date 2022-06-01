from classifier import Classifier
from data import Data
from node import Node
from queue import Queue

from validator import Validator

class Tree:
    
    def expandNode(self):
        if len(self.toExpand) == 0:
            return

        node: Node = self.toExpand[0]
        del self.toExpand[0]
        # for i in node.children:
        #     print("in here")
        #     print(i.currFeatures)
        if len(node.remainingFeatures) != 0:
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
                found = 0
                for j in range(len(self.tree)):
                    if self.tree[j].currFeatures == newNode.currFeatures and self.tree[j].remainingFeatures == newNode.remainingFeatures:
                        found = 1
                        node.children.append(self.tree[j])
                        self.tree[j].parent.append(node)
                        break
                if found == 0:
                    for j in range(len(self.toExpand)):
                        if self.toExpand[j].currFeatures == newNode.currFeatures and self.toExpand[j].remainingFeatures == newNode.remainingFeatures:
                            found = 1
                            node.children.append(self.toExpand[j])
                            self.toExpand[j].parent.append(node)
                if found == 0:
                    node.children.append(newNode)
                    self.toExpand.append(newNode)
                if newNode.depth > self.depth:
                    self.depth = newNode.depth
                

        # for i in node.children:
        #     print(i.currFeatures)  
        if self.root == None and (len(node.parent) == 0):
            self.root = node      
        self.tree.append(node)
        self.expandNode()
        return
        
            

    def __init__(self, features: list, validator: Validator):
        # self.data = data
        self.validator = validator
        self.features = features
        self.selected = []
        self.toExpand = []
        self.depth = 0
        self.tree = []
        self.root = None
        initial = Node([], self.features, 0, self.validator)
        self.toExpand.append(initial)
        self.expandNode()
        self.end = self.tree[-1]

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

    def ForwardSelection(self):
        highest = -1
        selected = {}
        
        node: Node = self.tree[0]
        print("Using no features, ie " + node.currFeatures.__str__() + ", accuracy is " + str(node.evaluation) + "%\n")
        highest = node.evaluation
        selected[highest] = node.currFeatures
        while len(node.children) != 0:
            maxVal = -1
            maxCurr = []
            maxNode = None
            for i in node.children:
                if i.evaluation > maxVal:
                    maxVal = i.evaluation
                    maxCurr = i.currFeatures
                    maxNode = i
                print("Using feature(s) " + i.currFeatures.__str__() + " accuracy is " + str(i.evaluation) + "%")
            selected[maxVal] = maxCurr
            if maxVal > highest:
                highest = maxVal
            print("\n")
            if maxVal < highest:
                print ("(Warning, selecting best feature set, " + maxCurr.__str__() + ", with accuracy " + str(maxVal) + "%" + " will decrease accuracy from " + str(highest) + "%!)")
            print("Feature set " + maxCurr.__str__() + " was best, accuracy is " + str(maxVal) + "%\n")    
            node = maxNode

        return (highest, selected[highest])
    
    def BackwardsElimination(self):
        highest = -1
        selected = {}
        
        node: Node = self.tree[-1]
        print("Using all features, ie " + node.currFeatures.__str__() + ", accuracy is " + str(node.evaluation) + "%\n")
        highest = node.evaluation
        selected[highest] = node.currFeatures
        while len(node.parent) != 0:
            maxVal = -1
            maxCurr = []
            maxNode = None
            for i in node.parent:
                if i.evaluation > maxVal:
                    maxVal = i.evaluation
                    maxCurr = i.currFeatures
                    maxNode = i
                print("Using feature(s) " + i.currFeatures.__str__() + " accuracy is " + str(i.evaluation) + "%")
            selected[maxVal] = maxCurr
            if maxVal > highest:
                highest = maxVal
            print("\n")
            if maxVal < highest:
                print ("(Warning, selecting best feature set, " + maxCurr.__str__() + ", with accuracy " + str(maxVal) + "%" + " will decrease accuracy from " + str(highest) + "%!)")
            print("Feature set " + maxCurr.__str__() + " was best, accuracy is " + str(maxVal) + "%\n")    
            node = maxNode

        return (highest, selected[highest])
    
    def solve(self, alg):
        print("\nBeginning Search\n")
        solution = 0
        if alg == 1:
            solution = self.ForwardSelection()
        else:
            solution = self.BackwardsElimination()

        print("Finished search!!! The best feature subset is " + solution[1].__str__() + " with an accuracy of " + str(solution[0]) + "%") 
