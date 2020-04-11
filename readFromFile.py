# Michael Gromski
# This program reads data from a text file and converts it to a useful form and makes a contour plot
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib


file_name = input("Enter the name of the file you want to read from: ")
fvar = open(file_name,"r")  # opens file

dataList = []
data = []

for line in fvar: # reads line by line and creates a nested list        #Reads Data from file and converts it to a usable nested list
    line = line.split()
    dataList.append(line)
for i in range(0, len(dataList)):   # converts all values to floats
    data.append([])
    for j in range(0,len(dataList[i])):
        b = float(dataList[i][j])
        data[i].append(b)

zPlots = []

for list in data:     # Converts the nested list into a format that can be used for contour plots
    i = 0
    j = 0
    frame = [[0 for x in range(10)] for y in range(10)]
    for elem in list:
        frame[i][j] = elem
        if j == 9:
            j = 0
            i += 1
        else:
            j += 1
    zPlots.append(frame)
a = 0
b = 5 #set frame you want to see here
matplotlib.style.use('default')     # Creates Contour plot

fig = plt.figure()
ax = fig.add_subplot(111)
u = np.linspace(0,9,10)
x, y = np. meshgrid(u,u)
breaks = np.linspace(-1,1,10)
z = zPlots[b]
levels = [20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
ax.contourf(x,y,z,levels = levels, cmap='RdBu_r')#cm.Greys_r
cp = ax.contourf(x,y,z,levels=levels)   # Color Bar
cb = fig.colorbar(cp)
cb.set_label('Temperature in Celsius')
plt.xlabel('Inches')
plt.ylabel('Inches')
plt.title('Thermal map of Aluminum Plate')
plt.show()

