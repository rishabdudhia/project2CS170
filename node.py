import random as rm

class Node:

    def evalFunc(self, currList: list):
        return rm.randint(0,100)

    def __init__(self, current: list, rem: list, parent):
        self.currFeatures = current
        self.currFeatures.sort()
        self.remainingFeatures = rem
        self.remainingFeatures.sort()
        self.evaluation = self.evalFunc(self.currFeatures)
        self.children = []
        if type(parent) == Node:
            self.parent = [parent]
        elif parent == 0:
            self.parent = []
        if type(parent) != Node:
            self.depth = 0
        else:
            self.depth = self.parent[0].depth + 1
