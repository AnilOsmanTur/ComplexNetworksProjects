#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:51:30 2017

@author: anilosmantur

Visiualization functions
"""

import networkx as nx
import matplotlib.pyplot as plt

def drawCommunityGraph(G, pos, part, fgSize, nodeSize=35):
    size = float(len(set(part.values())))
    print ('Found community count: ', size)
    count = 0.
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    for com in set(part.values()) :
        count = count + 1.
        list_nodes = [nodes for nodes in part.keys() if part[nodes] == com]
        values = [ (count / size) for nodes in list_nodes]
        nodes = nx.draw_networkx_nodes(G, 
                                       pos,
                                       list_nodes,
                                       cmap=plt.get_cmap('jet'),
                                       with_labels=False,
                                       node_size = nodeSize,
                                       node_color = values,
                                       vmin=0.0, vmax=1.0 ) # color map magma
        nodes.set_edgecolor('black')
        nodes.set_linewidth(1.0)
    
    
    edges = nx.draw_networkx_edges(G, pos, alpha=0.5)
    edges.set_linewidth(0.5)
    plt.show()
    print('Printing community layout finished')

def drawCommunityGraphSave(G, pos, part, fgSize, name):
    size = float(len(set(part.values())))
    print ('Found community count: ', size)
    count = 0.
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    for com in set(part.values()) :
        count = count + 1.
        list_nodes = [nodes for nodes in part.keys() if part[nodes] == com]
        values = [ (count / size) for nodes in list_nodes]
        nodes = nx.draw_networkx_nodes(G, 
                                       pos,
                                       list_nodes,
                                       cmap=plt.get_cmap('jet'),
                                       with_labels=False,
                                       node_size = 35,
                                       node_color = values,
                                       vmin=0.0, vmax=1.0 ) # color map magma
        nodes.set_edgecolor('black')
        nodes.set_linewidth(1.0)
    
    
    edges = nx.draw_networkx_edges(G, pos, alpha=0.5)
    edges.set_linewidth(0.5)
    
    plt.savefig('graphs/' + name +'_net_communities.png')
    print('Printing community layout finished')
    
def drawCentralityGraph(G, pos, cent, fgSize, nodeSize=35):
    count = 0.
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    for com in set(cent.values()) :
        count = count + 1.
        list_nodes = [nodes for nodes in cent.keys() if cent[nodes] == com]
        values = [ (400 * com) for nodes in list_nodes]
        nodes = nx.draw_networkx_nodes(G, 
                                       pos,
                                       list_nodes,
                                       cmap=plt.get_cmap('jet'),
                                       with_labels=False,
                                       node_size = values,
                                       node_color = values,
                                       vmin=0.0, vmax=1.0 ) # color map magma
        nodes.set_edgecolor('black')
        nodes.set_linewidth(1.0)
    
    
    edges = nx.draw_networkx_edges(G, pos, alpha=0.5)
    edges.set_linewidth(0.5)
    plt.show()
    print('Printing centrality layout finished')

def drawCentralityGraphSave(G, pos, cent, fgSize, name='', c_type=''):
    count = 0.
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    for com in set(cent.values()) :
        count = count + 1.
        list_nodes = [nodes for nodes in cent.keys() if cent[nodes] == com]
        values = [ (400 * com) for nodes in list_nodes]
        nodes = nx.draw_networkx_nodes(G, 
                                       pos,
                                       list_nodes,
                                       cmap=plt.get_cmap('jet'),
                                       with_labels=False,
                                       node_size = values,
                                       node_color = values,
                                       vmin=0.0, vmax=1.0 ) # color map magma
        nodes.set_edgecolor('black')
        nodes.set_linewidth(1.0)
    
    
    edges = nx.draw_networkx_edges(G, pos, alpha=0.5)
    edges.set_linewidth(0.5)
    plt.savefig('graphs/' + name +'_net_'+ c_type + '.png')
    print('Printing centrality layout finished')
    
def nxDrawCommunityGraph(G, pos, coms, fgSize, nodeSize=35):
    size = len(coms)
    print ('community count: ', size)
    count = 0.
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    for com in coms :
        count = count + 1.
        list_nodes = [nodes for nodes in com]
        values = [ (count / size) for nodes in list_nodes]
        nodes = nx.draw_networkx_nodes(G, 
                                       pos,
                                       list_nodes,
                                       cmap=plt.get_cmap('jet'),
                                       with_labels=False,
                                       node_size = nodeSize,
                                       node_color = values,
                                       vmin=0.0, vmax=1.0 ) # color map magma
        nodes.set_edgecolor('black')
        nodes.set_linewidth(1.0)
    
    
    edges = nx.draw_networkx_edges(G, pos, alpha=0.5)
    edges.set_linewidth(0.5)
    plt.show()
    print('Printing community layout finished')

    
def drawGraph(G, pos, fgSize, nodeSize=35):
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=nodeSize, node_color='red')
    nodes.set_edgecolor('black')
    nodes.set_linewidth(1.0)
    edges = nx.draw_networkx_edges(G, pos, edge_color='blue')
    edges.set_linewidth(0.5)
    plt.show()
    print('Printing layout finished')
    
def drawGraphSave(G, pos, fgSize, name=''):
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=35, node_color='red')
    nodes.set_edgecolor('black')
    nodes.set_linewidth(1.0)
    edges = nx.draw_networkx_edges(G, pos, edge_color='blue')
    edges.set_linewidth(0.5)
    plt.savefig('graphs/' + name +'_net.png')
    print('Printing layout finished')
    
def drawEgoGraph(G, pos, egoNode, fgSize):
    plt.figure(figsize=(fgSize, fgSize))
    plt.axis('off')
    plt.margins(tight=True)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=35, node_color='green')
    nodes.set_edgecolor('black')
    nodes.set_linewidth(1.0)
    edges = nx.draw_networkx_edges(G, pos, edge_color='blue')
    edges.set_linewidth(0.5)
    plt.show()
    print('Printing Ego layout finished')
    
def centralityPlot(cent, fgSize):
    plt.figure(figsize=(fgSize, fgSize))
    plt.margins(tight=True)
    cent = sorted(cent.items())
    values = [ c for (node, c) in cent]
    nodes = [ node for (node, c) in cent]
    plt.plot(nodes, values)
    plt.show()
    print('Printing Centrality Plot Finished')
    
def centralityPlotSave(cent, fgSize, name='', c_type=''):
    plt.figure(figsize=(fgSize, fgSize))
    plt.margins(tight=True)
    cent = sorted(cent.items())
    values = [ c for (node, c) in cent]
    nodes = [ node for (node, c) in cent]
    plt.plot(nodes, values)
    plt.savefig('graphs/' + name +'_net_plot_'+ c_type + '.png')
    print('Printing Centrality Plot Finished')
