import operator


def main():
    data = []

    file_handle = open("Jobs.txt", 'r')

    for line in file_handle:
        weight_i = int(line.split()[0])
        length_i = int(line.split()[1])
        diff = weight_i - length_i
        ratio = weight_i / length_i
        data.append([weight_i, length_i, diff, ratio])

    file_handle.close()
    print("ratio:", Scheduler(data, True))
    print("difference:", Scheduler(data, False))




def Scheduler(data, ratio):

    if not ratio:
        data = sorted(data, key = operator.itemgetter(2,1), reverse = True)
    else:
        data = sorted(data, key = operator.itemgetter(3,1), reverse = True)

    completionTime = 0
    sum = 0
    #print (data)

    for item in data:
        completionTime += item[1]
        sum += completionTime*item[0]

    return sum


main()
#ratio: 67311454237
#difference: 69119377652