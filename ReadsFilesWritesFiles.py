#Michael Gromski
# This program reads data off of file and takes the useful data then orders it in a text document

file_read = input("Enter the name of the file you want to read from: ")
file_write = input("Enter the name of the file you want to write to: ")
fvar = open(file_read,"r")
fvar1 = open(file_write,"w")

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
a = 0
for b in range(0,len(data)):
    
    print(data[a][0])
    '''
    print(data[a][56])
    print(data[a][66])
    print(data[a][76])
    print(data[a][86])
    print(data[a][96])
    print("\n")
    '''
    """
    fvar1.write("%s i \n" % str(data[a][48]))
    fvar1.write("%s j -1\n" % str(data[a][38]))
    fvar1.write("%s j+1 \n" % str(data[a][58]))
    fvar1.write("%s I-1 \n" % str(data[a][47]))
    fvar1.write("%s I+1 \n" % str(data[a][49]))
    fvar1.write("\n")
    """
    fvar1.write("%s \n" % str(data[a][48]))

    #fvar1.write("\n")
    
    a += 1
fvar.close()
fvar1.close()

