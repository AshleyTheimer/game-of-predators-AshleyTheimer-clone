import matplotlib.pyplot as plt
import numpy as np

#file_path = 'GOLQ2.csv'
#file_path = 'GOLQ2Try.csv'
#file_path = 'GOLQ2Accum2.csv'
file_path = 'GOLQ2Indi.csv'
file_path = 'GOLQ2WeightedRepo.csv'
with open(file_path, 'r', encoding='utf-8') as file:
    lineData = file.readlines()
   
lines = lineData[1:]  
dataList= []

dataDict = {
    0.5: [],
    1: [],
    1.5: [],
    2: [],
    2.5: [],
    3: [],
    3.5: [],
    4: []
}

for line in lines:
    row = line.strip()
    split = row.split(",")
    for num in range(len(split)):
        split[num] = float(split[num])
        key = float(split[0])
        num = float(split[1])
        print("key", key, "num:", num)
        dataDict[key].append(num)

fig, ax = plt.subplots()

ax.boxplot(dataDict.values())
ax.set_xticklabels(dataDict.keys())

plt.show()





'''


# Print the updated dictionary to see the results
print(dataDict)


keys = dataDict.keys()
avgs = [dataDict[key][1] for key in keys]
std_dev = [dataDict[key][2] for key in keys]
std_err = [dataDict[key][3] for key in keys]


fig, ax = plt.subplots()

ax.bar(keys, avgs, width= 0.4)
ax.errorbar(keys, avgs, yerr=std_dev, fmt=".", color="y")
ax.errorbar(keys, avgs, yerr=std_err, fmt=".", color="r")

ax.set_ylabel('Average Predator Life')
ax.set_xlabel('Stock Gained From Eating')
ax.set_title('Averge Predator Lifespan per Stock Gained from Eating')
plt.show()
'''