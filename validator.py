from classifier import Classifier
from data import Data

class Validator:

    def __init__(self, featureList: list, nearestNeighbor: Classifier, data: Data):
        self.data = data.data
        self.numInstances = len(self.data)
        self.classifier = nearestNeighbor
        self.leaveOut = [] #ith element is list without ith instance from self.data
        for i in range(len(self.data)):
            temp = []
            for j in range(len(self.data)):
                if i == j: continue
                temp.append(self.data[j])
            self.leaveOut.append(temp)
        self.accuracy = self.validate()

    def validate(self):
        numCorrect = 0
        for i in range(len(self.data)):
            self.classifier.train(self.leaveOut[i])
            iFeatures = []
            iClass = 0.0
            for j in range(len(self.data[i])):
                if j == 0:
                    iClass = self.data[i][j]
                    continue
                iFeatures.append(self.data[i][j])
            predictedClass = self.classifier.test(iFeatures, i)
            if iClass == predictedClass:
                numCorrect += 1
            self.classifier.clear()

        