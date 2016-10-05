import heapq as heap
import math


#Initializing global variables

def main():

    datalow =[]
    datahigh = []
    count = 0
    summedian = 0

    file_handle = open("Median.txt", 'r')
    for line in file_handle:
        data = int(line.split()[0])
        count+=1

        #inserting data stream into two heaps
        if len(datalow)==0:
            heap.heappush(datalow,-data)
        else:
            if data <= -datalow[0]:
                heap.heappush(datalow,-data)
            else:
                heap.heappush(datahigh,data)

        #maintaining the invariant of the heap size
        while abs(len(datalow) - len(datahigh)) > 1:
            if len(datalow) > len(datahigh):
                datapop = -heap.heappop(datalow)
                heap.heappush(datahigh, datapop)
            else:
                datapop=heap.heappop(datahigh)
                heap.heappush(datalow, -datapop)

        if count%2 == 0:
            index = count/2
        else:
            index = (count + 1)/2

        if index <=len(datalow):
            median = -datalow[0]
        else:
            median = datahigh[0]
        print (index, median)


        summedian += median

    print (summedian % 10000)


#    print("Datalow", datalow)
#    print("Datahigh", datahigh)
 #   print(len(datalow), len(datahigh))

main()