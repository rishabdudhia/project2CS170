from cmath import inf
from cmath import sqrt
from data import Data

class Classifier: 

    def __init__(self, data: Data):
        self.allData = data
        # self.trainingData = []
        self.leaveOut = -1
        
    
    def train(self, leaveOut: int):
        # self.trainingData.clear()
        # for i in range(len(self.allData.data)):
        #     if i == leaveOut: continue
        #     self.trainingData.append(self.allData.data[i])
        self.leaveOut = leaveOut

    def test(self, instanceFeatures: list, currFeatures: list):
        minDist = inf
        classMin = 0.0

        i = 0
        while i < (len(self.allData.data) ):
            if i == self.leaveOut: 
                i += 1
                continue
            distance = 0.0
            for j in range(len(currFeatures)):
                distance += (abs(instanceFeatures[currFeatures[j]] - self.allData.data[i][currFeatures[j]+1])) ** 2
            distance = abs(sqrt(distance))
            if distance < minDist:
                minDist = distance
                classMin = self.allData.data[i][0]
            i += 1
        return classMin
