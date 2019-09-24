import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_val = [1, 2, 3, 4, 5]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(input_val, squares, linewidth=3)

#chart title and labels axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize=14)

#tick size
ax.tick_params(axis='both', labelsize=24)

plt.show()

