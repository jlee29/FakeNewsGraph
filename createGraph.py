import json
import snap

def main():
	domainToNodeID = json.load(open("domainToNodeID_ALL.txt"))
	nodeIDToDomain = {v: k for k, v in domainToNodeID.iteritems()}

	LinkGraph = snap.LoadEdgeList(snap.PNGraph, "LinkGraph_ALL.txt", 0, 1)

	print("Number of nodes: %d" % (LinkGraph.GetNodes()))
	print("Number of edges: %d" % (LinkGraph.GetEdges()))	

	nodesToPrune = list()
	for Node in LinkGraph.Nodes():
		if Node.GetInDeg() <= 5:
			nodesToPrune.append(Node.GetId())

	for nodeToPrune in nodesToPrune:
		LinkGraph.DelNode(nodeToPrune)

	print("Number of nodes after pruning: %d" % (LinkGraph.GetNodes()))
	print("Number of edges after pruning: %d" % (LinkGraph.GetEdges()))	

	snap.SaveEdgeList(LinkGraph, 'LinkGraph_ALL_pruned.txt')

	# print("Number of nodes: %d" % (LinkGraph.GetNodes()))
	# print("Number of edges: %d" % (LinkGraph.GetEdges()))	

	# NIdHubH = snap.TIntFltH()
	# NIdAuthH = snap.TIntFltH()
	# HubKeyV = snap.TIntV()
	# AuthKeyV = snap.TIntV()

	# snap.GetHits(LinkGraph, NIdHubH, NIdAuthH)
	# NIdHubH.SortByDat()
	# NIdAuthH.SortByDat()

	# NIdHubH.GetKeyV(HubKeyV)
	# NIdAuthH.GetKeyV(AuthKeyV)

	# lengthOfHubKeys = HubKeyV.Len()
	# lengthOfAuthKeys = AuthKeyV.Len()

	# print("Top hubs:")
	# for i in range(1,10):
	# 	print(nodeIDToDomain[HubKeyV[lengthOfHubKeys-i]])

	# print("Top authorities:")
	# for i in range(1,10):
	# 	print(nodeIDToDomain[AuthKeyV[lengthOfAuthKeys-i]])	



if __name__ == '__main__':
	main()