import matplotlib.pyplot as plt

years_count = {'8059': 43, '1901': 9, '2037': 4, '2015': 27940, '2014': 14509, '2016': 3524722, '2011': 3713, '2010': 4599, '2013': 4524, '2012': 4287, '1957': 1, '1970': 27, '2002': 8, '2003': 28, '2000': 2, '2001': 3, '2006': 102, '2007': 103, '2004': 6, '2005': 35, '2008': 1844, '2009': 8285}

adjusted_years = {}

year_keys = [int(year) for year in years_count.keys()]
plt.bar(year_keys, years_count.values(), color='g', log=True)

plt.xlabel('Year')
plt.ylabel('References')
plt.title('Links References by Year')

plt.show()
