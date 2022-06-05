import random as rm
from classifier import Classifier
from data import Data
from validator import Validator

class Node:

    def evalFunc(self, currList: list, validator: Validator):
        if len(currList) == 0:
            return validator.classifier.allData.defaultRate * 100
        return validator.validate(currList) * 100
        # return rm.randint(0,100)

    def __init__(self, current: list, rem: list, parent, validator: Validator):
        self.currFeatures = current
        self.currFeatures.sort()
        self.remainingFeatures = rem
        self.remainingFeatures.sort()
        self.evaluation = self.evalFunc(self.currFeatures, validator)
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
