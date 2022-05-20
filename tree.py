from platform import node
from node import Node
from queue import Queue

class Tree:
    
    def expandNode(self):
        if self.toExpand.qsize() == 0:
            return

        node: Node = self.toExpand.get()
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
                newNode = Node(curr, rem, 0)
                if newNode.depth > self.depth:
                    self.depth = newNode.depth
                node.children.append(newNode)
                newNode.parent.append(node)
                self.toExpand.put(newNode)

        # for i in node.children:
        #     print(i.currFeatures)  
        if self.temproot == None and (len(node.parent) == 0):
            self.temproot = node      
        self.temptree.append(node)
        self.expandNode()
        return

        
    def minimizeTree(self):
        i = 0
        count = 0
        while i < len(self.temptree):
            if self.temptree[i].minimized == 1: 
                count += 1
                i += 1
                continue
            for j in range(i+1,len(self.temptree)):
                # if i == j: continue
                if self.temptree[j].minimized == 1: #unnecessary i think
                        continue
                if self.temptree[i].depth == self.temptree[j].depth and self.temptree[i].currFeatures == self.temptree[j].currFeatures and self.temptree[i].remainingFeatures == self.temptree[j].remainingFeatures:
                    for k in self.temptree[j].children:
                        if (k in self.temptree[i].children) and (k.minimized == 0):
                            continue
                        else:
                            self.temptree[i].children.append(k)
                    for k in self.temptree[j].parent:
                        if (k in self.temptree[i].parent) and (k.minimized == 0):
                            continue
                        else:
                            self.temptree[i].parent.append(k)
                    self.temptree[j].minimized = 1
            
            self.tree.append(self.temptree[i])
            i += 1

    def cleanTree(self):
        for i in self.tree:
            j = 0
            while j < len(i.parent):
                k = j + 1
                while k < len(i.parent):
                    if i.parent[j].currFeatures == i.parent[k].currFeatures:
                        del i.parent[j]
                        continue
                    k += 1
                j += 1
            j = 0
            while j < len(i.children):
                k = j + 1
                while k < len(i.children):
                    if i.children[j].currFeatures == i.children[k].currFeatures:
                        del i.children[j]
                        continue
                    k += 1
                j += 1
        j = 0
        while j < len(self.tree[-1].parent):
            k = j + 1
            while k < len(self.tree[-1].parent):
                if self.tree[-1].parent[j].currFeatures == self.tree[-1].parent[k].currFeatures:
                    del self.tree[-1].parent[j]
                    continue
                k += 1
            j += 1
        
            

    def __init__(self, features: list):
        self.features = features
        self.selected = []
        self.temptree = []
        self.toExpand = Queue()
        empty = []
        self.temproot = Node(empty, self.features, 0)
        self.depth = 0
        self.toExpand.put(self.temproot)
        self.expandNode()
        self.tree = []
        self.minimizeTree()
        self.cleanTree()
        self.root = self.tree[0]
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

        # q = Queue()
        # q.put(self.root)
        # node: Node = None
        # while q.qsize() > 0:
        #     node = q.get()
        #     print("curr: " + node.currFeatures.__str__())
        #     for i in node.children:
        #         print("child: " + i.currFeatures.__str__())
        #         q.put(i)
            
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
                print ("(Warning, selecting best feature set, " + maxCurr.__str__() + ", with accuracy " + str(maxVal) + "%" + " will decrease accuracy!)")
                return (highest, selected[highest])
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
                print ("(Warning, selecting best feature set, " + maxCurr.__str__() + ", with accuracy " + str(maxVal) + "%" + " will decrease accuracy!)")
                return (highest, selected[highest])
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
