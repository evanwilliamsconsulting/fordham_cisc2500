def findWordInString(aWord,aString):
    lenWord = len(aWord)
    lenString = len(aString)
    findArray = []
    for j in range(0,lenString+1):
	k = j + lenWord
        if aWord == aString[j:k]:
	    # Found aWord
            findArray.append(j)
    print(findArray)

findWordInString("CAT","ACATAGCTCATAACCTT")
