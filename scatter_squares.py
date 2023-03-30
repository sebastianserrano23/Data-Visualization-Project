from shutil import which
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s = 200)

# set chart titles and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=24)

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()