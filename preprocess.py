import csv
from datetime import datetime
from urlparse import urlparse
import json
import snap

# 2016-09-18 09:05:09

def extractDomain(rawURL):
	parsedUrl = urlparse(rawURL)
	if parsedUrl.netloc.startswith('www.'):
		return parsedUrl.netloc[4:]
	return parsedUrl.netloc

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
	edgeCounts = {}

	progress = 0

	for i in [1, 2, 3, 5]: 
		min_date = -1
		max_date = -1
		with open("web-2016-09-links-clean-{}.txt".format(i)) as tsvfile:
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
							edgeCounts[(domainToNodeID[fromDomain],domainToNodeID[toDomain])] = 1
						else:
							edgeCounts[(domainToNodeID[fromDomain],domainToNodeID[toDomain])] = edgeCounts[(domainToNodeID[fromDomain],domainToNodeID[toDomain])] + 1
					except ValueError:
						pass
						print("whoops")
				# if row[1][:4] != None:
				# 	year = row[1][:4]
				# 	if year not in years: 
				# 		years[year] = 1
				# 	else:
				# 		years[year] += 1
				# 	if min_date == -1: 
				# 		min_date = row[1]
				# 		max_date = row[1]
				# 	else:
				# 		if row[1] < min_date:
				# 			min_date = row[1]
				# 		elif max_date < row[1]:
				# 			max_date = row[1]
				# 	progress += 1
				# if row[1][:4] == "2016": 
				# 	month = row[1][5:7]
				# 	if month not in months: 
				# 		months[month] = 1
				# 	else:
				# 		months[month] += 1

				progress += 1
				if progress % 10000 == 0:
					print progress
	# 	print min_date, max_date
	# print years
	# print months
	print edgeCounts
	with open('domainToNodeID_ALL.txt', 'w') as file:
		file.write(json.dumps(domainToNodeID))
	with open('edgeCounts_ALL.csv', 'w') as file:
		for k, v in edgeCounts.iteritems():
			file.write('{},{},{}\n'.format(k[0], k[1], v))
	snap.SaveEdgeList(LinkGraph, 'LinkGraph_ALL.txt')

if __name__ == '__main__':
	main()
