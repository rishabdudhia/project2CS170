from classifier import Classifier
from data import Data

class Validator:

    def __init__(self, nearestNeighbor: Classifier, data: Data):
        self.data = data.data
        # self.currFeatures = featureList
        # self.numInstances = len(self.data)
        self.classifier = nearestNeighbor
        # self.leaveOut = [] #ith element is list without ith instance from self.data
        # for i in range(len(self.data)):
        #     temp = []
        #     for j in range(len(self.data)):
        #         if i == j: continue
        #         temp.append(self.data[j])
        #     self.leaveOut.append(temp)
        # self.accuracy = self.validate()

    def validate(self, currFeatures: list):
        numCorrect = 0
        for i in range(len(self.data)):
            self.classifier.train(i)
            iFeatures = []
            iClass = 0.0
            for j in range(len(self.data[i])):
                if j == 0:
                    iClass = self.data[i][j]
                    continue
                iFeatures.append(self.data[i][j])
            predictedClass = self.classifier.test(iFeatures, currFeatures, i)
            if iClass == predictedClass:
                numCorrect += 1
        accuracy = numCorrect / len(self.data)
        return accuracy

        