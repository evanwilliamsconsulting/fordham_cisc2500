def findCommaSeparatedStrings(inputString):
    # Find the substrings in inputString separated by commas
    lengthOfInput = len(inputString)
    returnStrings = []
    aString= ''
    for i in range(0,lengthOfInput):
	if inputString[i] == ',':
            if len(aString) > 0:
		returnStrings.append(aString)
	    aString = ''
	else:
            aString += inputString[i]
    if len(aString) > 0:
	returnStrings.append(aString)
    return returnStrings

def findMaximumLengthOfWordInList(aList):
    # Loop through all words
    maximumLength = 0
    for word in aList:
        if maximumLength < len(word):
            maximumLength = len(word)
    return maximumLength

# Rotate the letters in a Word Jumble by 90 degrees
def rotateJumble90(jumbledList):
    results = []
    firstWord = jumbledList[0]
    lenOfWord = len(firstWord)
    for i in range(0,lenOfWord):
        newJumbledWord = ''
        for jumbledWord in jumbledList:
             aLetter = jumbledWord[i]
             newJumbledWord += aLetter
        results.append(newJumbledWord)
    return results

# Return Diagonals
#
#  A B C D
#  B C D C
#  C D C B
#  D C B A
#
# Answer: [A,BB,CCC,DDDD,CCC,BB,A]
#
#
# A B C
# B C B
# C B A
#
#
#

def returnDiagonalJumble(jumbledList):
    results = []
    firstWord = jumbledList[0]
    lenOfWord = len(firstWord)
    k = 1
    for k in range(2,lenOfWord*2+1):
        aNewWord = ''
        for i in range(1,lenOfWord+1):
            for j in range(1,lenOfWord+1):
	    # All Letters that belong in the line go on the line
	        newJumble = jumbledList[i-1]
	        if i + j == k:
                    aNewWord += newJumble[j-1]
        results.append(aNewWord)
    return(results)

def findWordInString(aWord,aString):
    lenWord = len(aWord)
    lenString = len(aString)
    findArray = []
    for j in range(0,lenString+1):
	k = j + lenWord
        if aWord == aString[j:k]:
	    # Found aWord
            findArray.append(j)
    return findArray

#
def checkForAllWordsInList(inputWordList,jumbledList):
    results = []
    for aWord in inputWordList:
        forward = []
        for aString in jumbledList:
            forward = findWordInString(aWord,aString)
            results.append(forward)
    return results

# Reverse Words In List
def reverseWordsInList(inputWordList):
    #
    reversedWordList = []
    for aWord in inputWordList:
	reversedWord = aWord[::-1] 
	reversedWordList.append(reversedWord)
    return reversedWordList

# solve a word jumble
def solveJumble(inputWords,jumbledStrings):
    # First Validate Input
    # Both Inputs should be strings
    if type(inputWords) is 'str':
        print("List of Input Words must be a string")
	return
    if type(jumbledStrings) is 'str':
	print("Jumbled Strings must be a string")
	return
    inputWordList = findCommaSeparatedStrings(inputWords)	
    jumbledList = findCommaSeparatedStrings(jumbledStrings)
    print(inputWordList)
    print(jumbledList)
    maximumLengthOfInputList = findMaximumLengthOfWordInList(inputWordList)
    print("Maximum Length of Input words is ",maximumLengthOfInputList)
    maximumLengthOfJumble = findMaximumLengthOfWordInList(jumbledList)
    inputWordListReversed = reverseWordsInList(inputWordList)
    print("Maximum Length of Jumble ",maximumLengthOfJumble)
    # Double check that all Jumbled Strings are the same length 
    for word in jumbledList:
	if len(word) != maximumLengthOfJumble:
            print("Jumble is not Square!") 
            return
    results = []
    # Check for all words horizontally
    horizontalResults = checkForAllWordsInList(inputWordList,jumbledList)
    results.append(horizontalResults)	
    reversedInputWordList = reverseWordsInList(inputWordList)
    horizontalBackwardResults = checkForAllWordsInList(inputWordListReversed,jumbledList)
    results.append(horizontalBackwardResults)
    #
    jumbleDiagonal = returnDiagonalJumble(jumbledList)
    #
    horizontalResults = checkForAllWordsInList(inputWordList,jumbleDiagonal)
    results.append(horizontalResults)	
    horizontalBackwardResults = checkForAllWordsInList(inputWordListReversed,jumbleDiagonal)
    results.append(horizontalBackwardResults)
    #
    verticalList =  rotateJumble90(jumbledList)
    verticalResults = checkForAllWordsInList(inputWordList,verticalList)
    results.append(verticalResults)	
    verticalBackwardResults = checkForAllWordsInList(inputWordListReversed,verticalList)
    results.append(horizontalBackwardResults)
    #
    jumbleDiagonal = returnDiagonalJumble(verticalList)
    horizontalResults = checkForAllWordsInList(inputWordList,jumbleDiagonal)
    results.append(horizontalResults)	
    horizontalBackwardResults = checkForAllWordsInList(inputWordListReversed,jumbleDiagonal)
    results.append(horizontalBackwardResults)
    return results
	    
# Test 1
#findWordInString("CAT","ACATAGCTCATAACCTT")
# Test 2
#jumbledStrings = "edoc,abdd,abcd,code"
#jumbledList = findCommaSeparatedStrings(jumbledStrings)
#print(jumbledList)
#result = rotateJumble90(jumbledList)
#result = returnDiagonalJumble(jumbledList)
#print(result)
# Test 3
#jumbledStrings = "edoc,abdd,abcd,code"
#jumbledList = findCommaSeparatedStrings(jumbledStrings)
##print(jumbledList)
#reversedList = reverseWordsInList(jumbledList)
#print(reversedList)

#results = solveJumble("this,cat,bear,code","edoc,abdd,abcd,code")
#print(results)

inputWords = "ALL,LOVE,TRAIN,TEAR,WORD,BEAR,RUG,NO,TIN,DUCK"
jumble = "LOTEAR,LORDRU,LVAUAG,FEICEE,TINKBY,IQDROW"
result = solveJumble(inputWords,jumble)
print(result)
