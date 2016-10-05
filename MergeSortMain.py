import math
from MergeSort import mergesort

file_handle = open("IntegerArray.txt", "r")
inputArray = []

for line in file_handle:
    inputArray.append(int(line))



#inputArray = [1, 3, 5, 2, 4, 6]

#inputArray2 = [7,9]
#inputArray.extend(inputArray2)

#print(inputArray)
#L = inputArray[0:mm]
#R = inputArray[mm:uu]

#print(L)
#print(R)
#print(len(inputArray), len(L), len(R))


#inputArray[1:3] = inputArray2
#print(inputArray)

x,y =mergesort(inputArray)
print(y)
#print(y)