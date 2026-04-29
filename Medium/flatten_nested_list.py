def flattenNestedList(nestedList):
    # isinstance is the inbuilt method in the python use to check data type
    flattenList=[]
    for listItem in nestedList:
        if isinstance(listItem,list):
            flattenList.extend(listItem)
        else:
            flattenList.append(listItem)
            
    return flattenList


nestedList=[10,[20,30,40],33,89,[90]]

print(flattenNestedList(nestedList))
            
# output: [10, 20, 30, 40, 33, 89, 90]