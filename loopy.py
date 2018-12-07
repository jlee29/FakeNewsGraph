import networkx as nx
import numpy as np
import pandas as pd
from networkx.algorithms import node_classification

def main():

    edges = pd.read_csv("edgeCounts_ALL.csv",delimiter=',')
    G = nx.from_pandas_edgelist(edges, 'id1', 'id2', ['weight'])

    G.node[9509]['label'] = 'C'
    G.node[4913]['label'] = 'C'
    G.node[23431]['label'] = 'C'
    G.node[3347]['label'] = 'C'
    G.node[76]['label'] = 'C'
    G.node[143988]['label'] = 'L'
    G.node[350]['label'] = 'L'
    G.node[2404]['label'] = 'L'
    G.node[14217]['label'] = 'L'
    G.node[121918]['label'] = 'L'
    
    # print(node_classification.harmonic_function(G)[136546])

    #136546

if __name__ == '__main__':
    main()   
