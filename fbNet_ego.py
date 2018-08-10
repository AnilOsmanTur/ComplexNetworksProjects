#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:33:22 2017

@author: anilosmantur
"""

import os
import community
import networkx as nx
from networkx.algorithms import community as nx_com
from networkx.algorithms import approximation as nx_approx
import matplotlib.pyplot as plt
import UtilitiesNetwork as un

print('library imports done')

FILE_NAME = '/home/anilosmantur/***/complex_networks/project/ego_facebook/facebook/'

edgeFiles = [file for file in os.listdir(FILE_NAME) if 'edges' in file]

egoNodes = [int(ego[:-6]) for ego in edgeFiles ]
egoNodes.sort()

del edgeFiles

for egoNode in egoNodes:
    edges = []
    with open(FILE_NAME+ str(egoNode) + '.edges') as netfile:
        print('file opened')
        for i, line in enumerate(netfile):
            words = line.split()
            edges.append((egoNode, (int(words[0]))))
            edges.append((egoNode, (int(words[1]))))
            edges.append((int(words[0]), int(words[1])))
        print('Reading edges finished')
        
    G = nx.Graph(edges)
    
    info = nx.info(G) + '\n'
    # drawing the graph
    pos = nx.spring_layout(G)
    un.drawGraphSave(G, pos, 8, 'ego_'+str(egoNode))
    plt.close()
    
    part = community.best_partition(G)
    size = float(len(set(part.values())))
    com = 'Found community count: ' + str(size) + '\n'
    mode = community.modularity(part, G)
    mode = 'Modularity: ' + str(mode) + '\n'
    un.drawCommunityGraphSave(G, pos, part, 8, 'ego_'+str(egoNode))
    plt.close()
    #part2 = nx_com.girvan_newman(G)
    ##perf = nx_com.performance(G, part2)
    ##print('Performance girvan_newman : ', perf)
    #coms = list(sorted(c) for c in next(part2))
    #un.nxDrawCommunityGraphSave(G, pos, coms, 8, gi)
    
    centb = nx.centrality.betweenness_centrality(G)
    un.centralityPlotSave(centb, 5, 'ego_'+str(egoNode), 'betweenness')
    un.drawCentralityGraphSave(G, pos, centb, 8, 'ego_'+str(egoNode), 'betweenness')
    plt.close()
    
    centd = nx.centrality.degree_centrality(G)
    un.centralityPlotSave(centd, 5, 'ego_'+str(egoNode), 'degree')
    un.drawCentralityGraphSave(G, pos, centd, 8, 'ego_'+str(egoNode), 'degree')
    plt.close()
    
    with open('sums/egoNet_' + str(egoNode) + 'sum.txt', 'w') as sumfile:
        sumfile.write(info)
        sumfile.write(com)
        sumfile.write(mode)