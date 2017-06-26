# main.py

#1.
#import data listing nodes
#import data listing edges

#2.
#with the edges data, replace all node names with corresponding node ids
# use list this to overwrite the edges data G.edges() in network_graph_and_sols.py

import pdb
import csv
import numpy as np

csv_nodes = open('nodes.csv','rb')
csv_edges = open('edges.csv','rb')
i_nodes = csv.reader(csv_nodes)
i_edges = csv.reader(csv_edges)
