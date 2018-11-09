import networkx as nx
import numpy as np
import pandas as pd
from networkx.algorithms import node_classification

def main():

    edges = pd.read_csv("edgeCounts_ALL.csv",delimiter=',')
    G = nx.from_pandas_edgelist(edges, 'id1', 'id2', ['weight'])

    print(G.node[9509]['neighbours'])

    # print(node_classification.harmonic_function(G)[136546])

    #136546

if __name__ == '__main__':
    main()   
