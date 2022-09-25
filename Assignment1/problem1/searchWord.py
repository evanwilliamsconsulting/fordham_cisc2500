def searchWord(search,input):
    #
    # https://www.w3schools.com/python/ref_string_find.asp
    newInput = input
    x = newInput.find(search)
    print(x)
    while x != -1:
        newInput = newInput[x+3:]
        print(newInput) 
        x = newInput.find(search)
	print(x)

searchWord("CAT","CBTATACTCATACATA")
#searchWord("CAT","CBTATACTC")
