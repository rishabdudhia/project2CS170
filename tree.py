from node import Node
from queue import Queue

class Tree:

    def add(self, node:Node):
        self.tree.append(node)
    
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
                newNode = Node(curr, rem, node)
                node.children.append(newNode)
                self.toExpand.put(newNode)

        # for i in node.children:
        #     print(i.currFeatures)  
        if self.root == None and (len(node.parent) == 0):
            self.root = node      
        self.tree.append(node)
        self.expandNode()
        return

        
    def minimizeTree(self):
        minimized = []
        i = 0
        j = 0
        #while loops?
        for i in range(len(self.tree)):
            for j in range(1, len(self.tree)):
                if self.tree[i].depth == self.tree[j].depth:
                    if self.tree[i].currFeatures == self.tree[j].currFeatures and self.tree[i].remainingFeatures == self.tree[j].remainingFeatures:
                        for k in self.tree[j].parent:
                            self.tree[i].parent.append(k)
                        self.tree.remove(self.tree[j])

    def __init__(self, features: list):
        self.features = features
        self.selected = []
        self.tree = []
        self.toExpand = Queue()
        empty = []
        self.root = Node(empty, self.features, 0)
        self.toExpand.put(self.root)
        self.expandNode()

    def printTree(self):
        printQ = Queue()
        node: Node = self.root
        printQ.put(node)
        while printQ.qsize() != 0:
            node = printQ.get()
            print("curr")
            print(node.currFeatures)
            print("rem")
            print(node.remainingFeatures)
            for i in node.children:
                printQ.put(i)
            
    
    
    def solve(self):
        while self.expanded != 1:
            pass