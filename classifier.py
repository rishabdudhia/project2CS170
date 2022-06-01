from cmath import inf
from cmath import sqrt
from data import Data

class Classifier: 

    def __init__(self, currFeatures: int):
        self.trainingData = []
        self.features = currFeatures
    
    def train(self, trainingData: list):
        self.trainingData = trainingData

    def test(self, instanceFeatures: list, currID: int):
        # distanceToInstance = []
        print(self.features)
        minDist = inf
        classMin = 0.0

        i = 0
        while i < (len(self.trainingData) ):
            distance = 0.0
            for j in range(len(self.features)):
                distance += (abs(instanceFeatures[self.features[j]] - self.trainingData[i][self.features[j]+1])) ** 2
            distance = abs(sqrt(distance))
            # distanceToInstance.append(distance)
            if distance < minDist:
                minDist = distance
                classMin = self.trainingData[i][0]
            i += 1
        
        return classMin


    
    def clear(self):
        self.trainingData.clear()
