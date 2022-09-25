# CICS2500-L01 Information and Data Management
# Evan J. Williams, Instructor
# September 17, 2022
# Function to find words in a string
def findWordInString(searchWord,inputString):
    match = False
    searchWordIndex = 0
    searchWordLength = len(searchWord)
    searchWordTestChar = searchWord[searchWordIndex]
    searchWordMatchSoFar = False
    searchWordMatchWholeWord = False
    inputStringPos = 0
    inputStringLen = len(inputString)
    for i in range(0,inputStringLen):
        inputChar = inputString[i]
        if inputChar == searchWordTestChar:
            searchWordMatchSoFar = True
            searchWordIndex += 1
            if searchWordIndex + 1 == searchWordLength:
                searchWordMatchWholeWord = True
                searchWordIndex = 0
                searchWordMatchSoFar = False
            if searchWordMatchWholeWord == True:
                print("Match Whole Word")
                print("at")
                print(inputStringPos - searchWordIndex)
                searchMatchWholeWord = False
		searchWordMatchWholeWord = False
		searchWordIndex = 0
        else:
             searchWordMatchSoFar = False
             searchWordIndex = 0
        inputStringPos += 1
        searchWordTestChar = searchWord[searchWordIndex]

findWordInString("CAT","CATGCTACATAGACATGC")
