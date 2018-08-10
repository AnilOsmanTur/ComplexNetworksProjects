from networkAOT import Network


def main():
    # net = Network(10)

    # net.createScaleFree(1000, 3, 5)  # n of nodes, link limit, core size
    # net.printDegrees()
    # net.plotDegreeDist()

    net = Network()
    net.createRandomNet(1000, 3, 100)  # n of nodes, probability threshold
    net.printDegrees()
    net.plotDegreeDist()


if __name__ == '__main__':
    main()
