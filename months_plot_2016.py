import matplotlib.pyplot as plt

months_count_2016 = {'02': 2756, '10': 738, '01': 3788, '06': 11530, '07': 17150, '04': 6452, '03': 6863, '08': 64469, '09': 3400380, '05': 10596}

#fig, ax = plt.subplots()
#ax.set_yscale('log')

month_keys = [int(month) for month in months_count_2016.keys()]
plt.bar(month_keys, months_count_2016.values(), color='g', log=True)

plt.xlabel('Month')
plt.ylabel('References')
plt.title('Links References by Month (2016)')

plt.show()
