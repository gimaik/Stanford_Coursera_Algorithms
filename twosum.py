
def computeTwoSums(data,target):

    twosumcount = 0

    for key in data:
        expectedkey = target - key

        if expectedkey < key:
            if hasTwoSum(data, target):
                twosumcount += data[expectedkey]

    return twosumcount

def hasTwoSum(data, target):
    for key in data:
        expectedkey = target - key
        if (expectedkey in data) and (expectedkey!=key):
            return True

def computeTwoSumRange(data, low, high):
    totaltwosums={}

    for k in range(low, high+1):
        if hasTwoSum(data, k):
            totaltwosums[k]=totaltwosums.get(k,0)+1

    return totaltwosums, len(totaltwosums)


def main():

    data={}
    arraydata=[]

    file_handle = open("2sum.txt", 'r')
    for line in file_handle:
        key = int(line.split()[0])
        data[key] = data.get(key,1) + 1
        arraydata.append(key)
    arraydata.sort()
    file_handle.close()

    x=computeTwoSumRange(data,-10000, 10000)
    print(x)

main()

#427