import matplotlib.pyplot as plt
import numpy as np

# got function from: https://www.geeksforgeeks.org/python-get-unique-values-list/
def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)


#file_path = 'GOLQ1.csv'
#file_path = 'GOLQ1Try.csv'
file_path = 'GOLQ1Accum.csv'
with open(file_path, 'r', encoding='utf-8') as file:
    lineData = file.readlines()
   
lines = lineData[1:]    
dataList= []

dataDict = {
    20: [[], 0, 0, 0],
    30: [[], 0, 0, 0],
    40: [[], 0, 0, 0],
    50: [[], 0, 0, 0],
    60: [[], 0, 0, 0],
    70: [[], 0, 0, 0],
    80: [[], 0, 0, 0],
    90: [[], 0, 0, 0],
    100: [[], 0, 0, 0],
    110: [[], 0, 0, 0],
}

for line in lines:
    row = line.strip()
    split = row.split(",")
    for num in range(len(split)):
        split[num] = int(split[num])
    key = int(split[1])
    dataDict[key][0].append(split[0])
    
for key in dataDict:
    values = dataDict[key][0] 
    dataDict[key][1] = sum(values) / len(values)  # Calculate the average
    dataDict[key][2] = np.std(values)
    dataDict[key][3] = np.std(values) / np.sqrt(len(values))
    

# Print the updated dictionary to see the results
print(dataDict)


keys = dataDict.keys()
avgs = [dataDict[key][1] for key in keys]
std_dev = [dataDict[key][2] for key in keys]
std_err = [dataDict[key][3] for key in keys]


fig, ax = plt.subplots()

ax.bar(keys, avgs, width= 4)
#ax.errorbar(keys, avgs, yerr=std_dev, fmt=".", color="y")
ax.errorbar(keys, avgs, yerr=std_err, fmt=".", color="r", label='Standard Error')

ax.set_ylabel('Average Number of Predators')
ax.set_xlabel('Stock to Reproduce')
ax.set_title('Max Number of Predators for Different Reproduction Stocks')
plt.legend(loc = 'upper right')
plt.show()
