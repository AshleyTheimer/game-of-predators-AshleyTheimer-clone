import matplotlib.pyplot as plt
import numpy as np

#file_path = 'GOLQ1.csv'
#file_path = 'GOLQ1Try.csv'
file_path = 'GOLQ1not.csv'
file_path = 'GOLQ3.csv'
with open(file_path, 'r', encoding='utf-8') as file:
    lineData = file.readlines()
   
lines = lineData[1:]    
dataList= []

dataDict = {
    20: [[], 0, 0],
    30: [[], 0, 0],
    40: [[], 0, 0],
    50: [[], 0, 0],
    60: [[], 0, 0],
    70: [[], 0, 0],
    80: [[], 0, 0],
    90: [[], 0, 0],
    100: [[], 0, 0],
    110: [[], 0, 0],
}

dataDict3 = {
    20: [[], 0, 0],
    30: [[], 0, 0],
    40: [[], 0, 0],
    50: [[], 0, 0],
    60: [[], 0, 0],
    70: [[], 0, 0],
    80: [[], 0, 0],
    90: [[], 0, 0],
    100: [[], 0, 0],
    110: [[], 0, 0],
}

for line in lines:
    row = line.strip()
    split = row.split(",")
    for num in range(len(split)):
        split[num] = int(split[num])
    key = int(split[0])
    dataDict[key][0].append(split[1])
    dataDict3[key][0].append(split[2])

print(dataDict)
   
for key in dataDict:
    values1 = dataDict[key][0]
    values3 = dataDict3[key][0]
    dataDict[key][1] = sum(values1) / len(values1)  # Calculate the average
    dataDict3[key][1] = sum(values3) / len(values3)  # Calculate the average
    dataDict[key][2] = np.std(values1) #/ np.sqrt(len(values1))
    dataDict3[key][2] = np.std(values3) #/ np.sqrt(len(values3))
    print(dataDict[key][2])

#fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(5, 7), height_ratios = [2, 2])
plt.figure(figsize=(7, 5))

keys = dataDict.keys()
avgs = [dataDict[key][1] for key in keys]
std_err = [dataDict[key][2] for key in keys]
plt.errorbar(keys, avgs, yerr=std_err, fmt='.', linewidth = 1, markersize = 9, color='red', label='Normal GOL')

avgs = [dataDict3[key][1] for key in keys]
std_err = [dataDict3[key][2] for key in keys]
plt.errorbar(keys, avgs, yerr=std_err, fmt='.', linewidth = 1, markersize = 9, color='blue', label='GOL With New Rule')

#ax3.bar(keys, avgs, width= 4)
#ax3.errorbar(keys, avgs, yerr=std_err, fmt=".", color="r")

plt.title("How The Max Number of Predators Change with New GOL Rules")
plt.ylabel('Average Maximum Number of Predators')
plt.xlabel('Stock to Reproduce')
plt.legend(loc = 'upper right')


plt.show()
