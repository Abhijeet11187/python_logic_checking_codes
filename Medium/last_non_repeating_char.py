def findFirstNonRepeatingCharacter(inputData):
    frequency_counter={}
    for char in inputData:
        frequency_counter[char]=frequency_counter.get(char,0)+1
    
    for char in reversed(frequency_counter):
        if frequency_counter[char]==1:
            return char   
    
            
        

inputData="aaabbcdefkk"
print(findFirstNonRepeatingCharacter(inputData))

#output is f