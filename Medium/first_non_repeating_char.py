def findFirstNonRepeatingCharacter(inputData):
    frequency_counter={}
    for char in inputData:
        frequency_counter[char]=frequency_counter.get(char,0)+1
    
    for char in frequency_counter:
        if frequency_counter[char]==1:
            return char   
    
            
        

inputData="aaabbcdef"
print(findFirstNonRepeatingCharacter(inputData))

# ouput is c