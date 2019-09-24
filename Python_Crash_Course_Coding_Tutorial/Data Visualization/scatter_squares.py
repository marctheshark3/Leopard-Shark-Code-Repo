import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y = [1, 4, 9, 16, 25]

x = range(1,1001)
y = [i**2 for i in x]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)

#chart title and labels axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize=14)

#tick size
ax.tick_params(axis='both', which='major', labelsize=24)

#plt.savefig('squares_plot.png', bbox_inches = 'tight')

plt.show()