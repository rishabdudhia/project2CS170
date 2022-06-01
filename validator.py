from classifier import Classifier
from data import Data

class Validator:

    def __init__(self, nearestNeighbor: Classifier, data: Data):
        self.data = data.data
        self.classifier = nearestNeighbor

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
            predictedClass = self.classifier.test(iFeatures, currFeatures)
            if iClass == predictedClass:
                numCorrect += 1
        accuracy = numCorrect / len(self.data)
        return accuracy

        