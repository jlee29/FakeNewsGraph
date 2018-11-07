import csv
from datetime import datetime
from urlparse import urlparse
import json
import snap

# 2016-09-18 09:05:09

def extractDomain(rawURL):
	parsedUrl = urlparse(rawURL)
	return '{uri.scheme}://{uri.netloc}/'.format(uri=parsedUrl)

def isUninteresting(url):
	if 'facebook' in url:
		return True
	elif 'instagram' in url:
		return True
	elif 'twitter' in url:
		return True
	elif 'google' in url:
		return True
	else:
		return False

def main():
	LinkGraph = snap.TNGraph.New()

	currID = 0
	domainToNodeID = {}

	progress = 0

	with open('web-2016-09-links-clean-1.txt') as tsvfile:
		linkReader = csv.reader(tsvfile, delimiter='\t')
		for row in linkReader:
			fromDomain = extractDomain(row[0])
			if isUninteresting(fromDomain):
				continue
			if fromDomain not in domainToNodeID:
				domainToNodeID[fromDomain] = currID
				LinkGraph.AddNode(currID)
				currID += 1

			uniqueToDomains = set()

			for link in row[2:]:
				try:
					toDomain = extractDomain(link)
					if isUninteresting(toDomain):
						continue
					if toDomain not in domainToNodeID:
						domainToNodeID[toDomain] = currID
						LinkGraph.AddNode(currID)
						currID += 1
					if toDomain not in uniqueToDomains:
						LinkGraph.AddEdge(domainToNodeID[fromDomain],domainToNodeID[toDomain])
						uniqueToDomains.add(toDomain)
				except ValueError:
					print("whoops")
			progress += 1
			if progress % 10000 == 0:
				print progress

	with open('domainToNodeID.txt', 'w') as file:
		file.write(json.dumps(domainToNodeID))
	snap.SaveEdgeList(LinkGraph, 'LinkGraph_1.txt')

if __name__ == '__main__':
	main()