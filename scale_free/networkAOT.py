import numpy as np
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.degree = 0

    def addAdjecent(self, x):
        if x not in self.adj:
            self.adj.append(x)
            self.degree += 1
            return x
        else:
            print(str(x) + " item is already a neighbor")
            return -1

    def delAdjecent(self, x):
        self.adj.remove(x)
        self.degree -= 1


class Network:
    def __init__(self, randomSeed=None):
        self.net = []
        self.netPrefList = []
        self.prefSize = 0
        self.random = random.Random()
        self.random.seed( randomSeed ) # if its none system time will be used

    def addPref(self, x):
        self.netPrefList.append(x)
        self.prefSize += 1

    def createScaleFree(self, n_node, l_link, n_core):  # n node for network l link for each node n core
        self.createCoreNodes(n_core)

        for i in range(n_core, (n_node + 1 - n_core)):
            node = Node(i)

            self.random.shuffle(self.netPrefList)
            for j in range(l_link):
                rand = self.random.randint(0, self.prefSize-1)
                pref = self.netPrefList[rand]
                connected = node.addAdjecent(pref)
                if connected != -1:
                    self.net[connected].addAdjecent(i)
                    self.addPref(connected)

            self.net.append(node)
            self.addPref(i)



    def createCoreNodes(self, n_core):

        for i in range(n_core):
            self.net.append(Node(i))
            self.addPref(i)

        for i in range(n_core):
            node = self.net[i]
            for j in range(n_core):
                if j != i:
                    node.addAdjecent(j)

    def degreeDistribution(self):
        degrees = []
        n_degrees = []
        for i in range(len(self.net)):
            node = self.net[i]
            degrees.append(node.degree)
            if node.degree not in n_degrees:
                n_degrees.append(node.degree)
        degrees.sort()
        print(degrees)
        n_degrees.sort()
        print(n_degrees)

        dist = np.zeros(len(n_degrees), dtype=np.float32)

        for i in range(len(n_degrees)):
            d_size = len(degrees)
            j = 0
            while  j < d_size:
                if n_degrees[i] == degrees[j]:
                    dist[i] += 1
                    degrees.remove(n_degrees[i])
                    j -= 1
                    d_size -= 1
                else:
                    break
                j += 1
        print(dist)
        dist = dist / len(self.net)
        print(dist)
        return (dist, n_degrees)


    def printDegrees(self):
        degrees = []
        for i in range(len(self.net)):
            node = self.net[i]
            degrees.append(str(node.degree) + ' ')
        print("".join(degrees))

    def plotDegreeDist(self):

        dict, degrees =self.degreeDistribution()

        plt.plot(degrees, dict)
        plt.ylim([dict.min(), dict.max()])
        plt.xlim([degrees[0], degrees[-1]])
        plt.ylabel("P(k)")
        plt.xlabel("Degrees")
        plt.show()


    def connectTwoNode(self, i, j, prob_a=1, prob_b=100):
        node1 = self.net[i]
        node2 = self.net[j]
        for x in range(prob_a):
            prob = self.random.randint(0, prob_b)
            if prob == 7:
                node1.addAdjecent(j)
                node2.addAdjecent(i)

    def createRandomNet(self, n_node, prob_a=1, prob_b=100):
        for i in range(0, n_node):
            node = Node(i)
            self.net.append(node)

        for i in range(n_node):
            for j in range(i+1, n_node):
                self.connectTwoNode(i, j, prob_a, prob_b)

