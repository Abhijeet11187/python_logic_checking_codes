def findMaxFromList(listData):
    max=0
    for num in listData:
        if(num>max):
            max=num
    return max

listData=[3,5,6,7,9,0]

print(findMaxFromList(listData))

#output 9