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


file_path = 'GOLQ2.csv'
#file_path = 'GOLQ2Try.csv'
#file_path = 'GOLQ2Accum.csv'
file_path = 'GOLQ2WeightedRepo.csv'
with open(file_path, 'r', encoding='utf-8') as file:
    lineData = file.readlines()
   
lines = lineData[1:]  
dataList= []

dataDict = {
    0.5: [[], 0, 0, 0],
    1: [[], 0, 0, 0],
    1.5: [[], 0, 0, 0],
    2: [[], 0, 0, 0],
    2.5: [[], 0, 0, 0],
    3: [[], 0, 0, 0],
    3.5: [[], 0, 0, 0],
    4: [[], 0, 0, 0]
}

for line in lines:
    row = line.strip()
    split = row.split(",")
    for num in range(len(split)):
        split[num] = float(split[num])
        key = float(split[0])
        num = float(split[1])
        print("num:", num)
        dataDict[key][0].append(num)

print(dataDict)

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

ax.bar(keys, avgs, width= 0.4)
#ax.errorbar(keys, avgs, yerr=std_dev, fmt=".", color="y")
ax.errorbar(keys, avgs, yerr=std_err, fmt=".", color="r", label='Standard Error')

ax.set_ylabel('Average Predator Life')
ax.set_xlabel('Stock Gained From Eating')
ax.set_title('Averge Predator Lifespan per Stock Gained from Eating')
plt.legend(loc = 'upper right')
plt.show()
