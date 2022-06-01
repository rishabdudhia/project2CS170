from cmath import inf
from cmath import sqrt
from data import Data

class Classifier: 

    def __init__(self, data: Data):
        self.allData = data
        self.trainingData = []
        
    
    def train(self, leaveOut: int):
        self.trainingData.clear()
        for i in range(len(self.allData.data)):
            if i == leaveOut: continue
            self.trainingData.append(self.allData.data[i])

    def test(self, instanceFeatures: list, currFeatures: list):
        minDist = inf
        classMin = 0.0

        i = 0
        while i < (len(self.trainingData) ):
            distance = 0.0
            for j in range(len(currFeatures)):
                distance += (abs(instanceFeatures[currFeatures[j]] - self.trainingData[i][currFeatures[j]+1])) ** 2
            distance = abs(sqrt(distance))
            if distance < minDist:
                minDist = distance
                classMin = self.trainingData[i][0]
            i += 1
        return classMin
