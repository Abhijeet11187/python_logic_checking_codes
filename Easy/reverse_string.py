def reverse_string(inputString):
    result=""
    for char in inputString:
        result=char+result
    return result

print(reverse_string("genai")) 
