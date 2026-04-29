def groupAnagramWords(wordsList):
    anagramWordsObj={}
    for word in wordsList:
        key="".join(sorted(word))
        anagramWordsObj.setdefault(key,[]).append(word)
    return anagramWordsObj.values()
    


inputData=['eat','tea','tan','ate','nat','bat']    
print(groupAnagramWords(inputData))


# Output is ([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])