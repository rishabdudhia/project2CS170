import random as rm
from classifier import Classifier
from data import Data
from validator import Validator

class Node:

    def evalFunc(self, currList: list, data: Data):
        nearestNeighbor = Classifier(currList)
        v = Validator(currList, nearestNeighbor, data)
        return v.accuracy

    def __init__(self, current: list, rem: list, parent, data: Data):
        self.currFeatures = current
        self.currFeatures.sort()
        self.remainingFeatures = rem
        self.remainingFeatures.sort()
        self.evaluation = self.evalFunc(self.currFeatures, data)
        self.children = []
        self.minimized = 0
        if type(parent) == Node:
            self.parent = [parent]
        elif parent == 0:
            self.parent = []
        if type(parent) != Node:
            self.depth = 0
        else:
            self.depth = self.parent[0].depth + 1
