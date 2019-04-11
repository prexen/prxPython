


def getTextFromFile(fileName):
    tempPriceString = ""
    myfileObject = open(fileName, "r")
    tempPriceString = myfileObject.read()
    return tempPriceString

def getPriceInTextFormat(searchTerm, textToSearch):
    sizeOfSearchParameter = len(searchTerm)
    startingIndex = textToSearch.find(searchTerm)
    totalChars = len(textToSearch)

    stringFinal = ""
    priceCounter = 0
    lastTwoDigits = False
    finalCounter = 0
    while(True):

        currentIndex = startingIndex + sizeOfSearchParameter + priceCounter
        if(currentIndex >= totalChars):
            break

        characterInString = textToSearch[startingIndex + sizeOfSearchParameter + priceCounter]
        if(characterInString == ','):
            lastTwoDigits = True
        if(lastTwoDigits):
            finalCounter += 1
            if(finalCounter > 3):
                break
        
        stringFinal += characterInString
        priceCounter += 1
    return stringFinal

def getPriceFromFileTeste(fileName):
    tempPriceString = ""
    tempPriceFloat = 0

    myfileObject = open(fileName, "r") 
    line = myfileObject.readline()
    cnt = 1
    while (line):
        if(cnt == 18):
            print("Line {}: {}".format(cnt, line.strip()))
            print(line.strip())#tira os whitespaces
                
            startCounDown = 0
            endcheckCounter = 0
            letterCounter = 0
            while(endcheckCounter < 3):
                currentChar = line[letterCounter]
                if(currentChar == ','):
                    startCounDown = 1
                    tempPriceString += "."
                else:
                    tempPriceString += currentChar

                if(startCounDown == 1):
                    endcheckCounter += 1
                
                letterCounter += 1
                
            
            print(tempPriceString)
            
            tempPriceFloat = float(tempPriceString)
            break

        line = myfileObject.readline()
        cnt += 1
    myfileObject.close()
    return tempPriceFloat


'''
texto = getTextFromFile("searchText.txt")
searchString = "BVMF: ITUB3"
finalPriceValue = float(getPriceInTextFormat(searchString, texto).replace(",","."))
print(finalPriceValue)
'''