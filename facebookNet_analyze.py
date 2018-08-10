#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:46:44 2017

@author: anilosmantur
"""

import community
import networkx as nx
from networkx.algorithms import community as nx_com
from networkx.algorithms import approximation as nx_approx
import matplotlib.pyplot as plt
import UtilitiesNetwork as un
print('library imports done')

FILE_NAME = '/home/anilosmantur/**/complex_networks/project/ego_facebook/facebook_combined.txt'

edges = []
with open(FILE_NAME) as netfile:
    print('file opened')
    for i, line in enumerate(netfile):
        words = line.split()
        edges.append((int(words[0]), int(words[1])))
    print('Reading edges finished')


fb_net = nx.Graph(edges)    
info = nx.info(fb_net) + '\n'

avgCluster_coef = nx.average_clustering(fb_net)
Cl_co = 'Estimation of avgerage clusternig coefficient:'+str(avgCluster_coef) + '\n'

dens = nx.density(fb_net)
dens = 'Density of network: ' + str(dens) + '\n'

#max_clique = nx_approx.max_clique(fb_net)
#print(max_clique)

# drawing the graph
pos = nx.spring_layout(fb_net)
un.drawGraphSave(fb_net, pos, 8, 'fbNet_')
plt.close()

part = community.best_partition(fb_net)
size = float(len(set(part.values())))
com = 'Found community count: ' + str(size) + '\n'
mode = community.modularity(part, fb_net)
mode = 'Modularity: ' + str(mode) + '\n'
un.drawCommunityGraphSave(fb_net, pos, part, 8, 'fbnet_')
del part
plt.close()


centb = nx.centrality.betweenness_centrality(fb_net)
un.centralityPlotSave(centb, 5, 'fbnet_', 'betweenness')
un.drawCentralityGraphSave(fb_net, pos, centb, 8, 'fbnet_', 'betweenness')
del centb
plt.close()

centd = nx.centrality.degree_centrality(fb_net)
un.centralityPlotSave(centd, 5, 'fbnet_', 'degree')
un.drawCentralityGraphSave(fb_net, pos, centd, 8, 'fbnet_', 'degree')
del centd
plt.close()

with open('sums/fbnet_sum.txt', 'w') as sumfile:
    sumfile.write(info)
    sumfile.write(Cl_co)
    sumfile.write(com)
    sumfile.write(mode)
    sumfile.write(dens)

# analyze the network
hist = nx.degree_histogram(fb_net)
plt.figure(figsize=(10, 10))
plt.plot(hist, linestyle=':')
plt.title('Degree Historam')
plt.savefig('fbNet_Degree.png')
plt.close()
print('Degree Historam finished')

lap_spec = nx.laplacian_spectrum(fb_net)
plt.plot(lap_spec)
plt.title('Eigenvalues of the Laplacian')
plt.savefig('fbNet_LapSpec.png')
plt.close()
print('Eigenvalues of the Laplacian')

adj_spec = nx.adjacency_spectrum(fb_net)
plt.plot(adj_spec)
plt.title('Eigenvalues of the Adjaceny')
plt.savefig('fbNet_AdjSpec.png')
plt.close()
print('Eigenvalues of the Adjaceny')

spec_ordering = nx.spectral_ordering(fb_net)
plt.plot(spec_ordering)
plt.title('Spectral Ordering')
plt.savefig('fbNet_SpecOrder.png')
plt.close()
print('Spectral Ordering')