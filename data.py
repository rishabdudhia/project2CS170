import json
import statistics

class Data:

    def __init__(self, file):
        t = self.convert(file)
        self.data:list = t[0]
        self.numFeatures = t[1]
        print("This dataset has " + str(self.numFeatures) + " features (not including the class attribute), with " + str(len(self.data)) + " instances.\n")
        self.meanFeatures = []
        self.stdFeatures = []
        print("Please wait while I normalize the data...")
        self.normalize()
        print("Done!")
        self.defaultRate = -1
        c1 = 0
        c2 = 0
        for i in range(len(self.data)):
            if self.data[i][0] == 1.0:
                c1 += 1
            else:
                c2+= 1
        
        if c1 > c2:
            self.defaultRate = c1 / len(self.data)
        else:
            self.defaultRate = c2 / len(self.data)

    def convert(self, file):
        file = "./data/" + file
        dict = []
        with open(file) as f:
            i = 0
            colCount = 0
            for l in f:
                last = ''
                counted = 0
                for j in range(len(l)):
                    if j < 5: continue
                    if l[j] == ' ' and counted == 0:
                        colCount += 1
                        counted = 1
                    elif l[j] == ' ' and counted == 1:
                        continue
                    elif l[j] != ' ':
                        counted = 0
                    if l[j] == '\n' and last != ' ':
                        break
                    elif l[j] == '\n' and last == ' ':
                        colCount -= 1
                        break
                    last = l[j]
                break
        with open(file) as f:
            i = 0
            for l in f:
                d = list(l.strip().split(None, colCount))
                dict.append(d)
                i += 1
        return (dict, colCount)
    
    def normalize(self):
        normalized = []
        for k in range(self.numFeatures):
            normalized.append([])
        for instance in self.data:
            for i in range(len(instance)):
                if i == 0: continue
                normalized[i - 1].append(instance[i])
        self.meanFeatures = []
        self.stdFeatures = []
        for i in range(len(normalized)):
            for j in range(len(normalized[i])):
                normalized[i][j] = float(normalized[i][j])
            self.meanFeatures.append(statistics.mean(normalized[i]))
            self.stdFeatures.append(statistics.stdev(normalized[i]))
        for i in range(len(normalized)):
            for j in range(len(normalized[i])):
                normalized[i][j] = (normalized[i][j] - self.meanFeatures[i]) / (self.stdFeatures[i])
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == 0: 
                    self.data[i][j] = float(self.data[i][j])
                    continue
                self.data[i][j] = normalized[j-1][i]


    