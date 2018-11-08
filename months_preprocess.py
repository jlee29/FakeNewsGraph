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
	elif 'youtube' in url:
		return True
	elif url == 'https://t.co/':
		return True
	else:
		return False

def main():
	LinkGraph = snap.TNGraph.New()

	currID = 0
	domainToNodeID = {}
	years = {}
	months = {}
	months_graph = {}

	progress = 0

	for i in [1, 2, 3, 5]: 
		min_date = -1
		max_date = -1
		with open("web-2016-09-links-clean-{}.txt".format(i)) as tsvfile:
			linkReader = csv.reader(tsvfile, delimiter='\t')
			for row in linkReader:
				if row[1][:4] == "2016": 
					month = row[1][5:7] 
					if month not in months_graph: 
						months_graph[month] = snap.TNGraph.New()
					curr_graph = months_graph[month]

					fromDomain = extractDomain(row[0])
					if isUninteresting(fromDomain):
						continue
					if fromDomain not in domainToNodeID:
						domainToNodeID[fromDomain] = currID
						curr_graph.AddNode(currID)
						currID += 1

					uniqueToDomains = set()

					for link in row[2:]:
						try:
							toDomain = extractDomain(link)
							if isUninteresting(toDomain):
								continue
							if toDomain not in domainToNodeID:
								domainToNodeID[toDomain] = currID
								curr_graph.AddNode(currID)
								currID += 1
							if toDomain not in uniqueToDomains:
								curr_graph.AddEdge(domainToNodeID[fromDomain],domainToNodeID[toDomain])
								uniqueToDomains.add(toDomain)
						except ValueError:
							pass
							print("whoops")
				# if row[1][:4] == "2016": 
				# 	month = row[1][5:7]
				# 	if month not in months: 
				# 		months[month] = 1
				# 	else:
				# 		months[month] += 1


				# if progress % 10000 == 0:
				# 	print progress
		print min_date, max_date
	print years
	print months
	with open('domainToNodeID_ALL.txt', 'w') as file:
		file.write(json.dumps(domainToNodeID))
	snap.SaveEdgeList(LinkGraph, 'LinkGraph_ALL.txt')

if __name__ == '__main__':
	main()
