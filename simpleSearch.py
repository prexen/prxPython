import requests
import prxResultParser
from html.parser import HTMLParser
from bs4 import BeautifulSoup

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        pass

    def handle_endtag(self, tag):
        pass
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)



def getPriceInGoogleSearchResult(searchTerm, textToSearch):
    sizeOfSearchParameter = len(searchTerm)
    startingIndex = textToSearch.find(searchTerm)

    stringBuild = ""
    priceCounter = 0
    lastTwoDigits = False
    finalCounter = 0
    while(True):
        characterInString = textToSearch[startingIndex + sizeOfSearchParameter + priceCounter]
        if(characterInString == ','):
            lastTwoDigits = True
        if(lastTwoDigits):
            finalCounter += 1
            if(finalCounter > 3):
                break
        
        stringBuild += characterInString
        priceCounter += 1

    
    return stringBuild


baseSearchTerm = "KNRI11"

url = "https://www.google.com/search?q=BVMF: " + baseSearchTerm

r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, "html.parser")
bodyText = soup.body.getText()

searchString = "BVMF:KNRI11&amp;"
#searchString = "(BVMF)"
#finalPriceValue = (prxResultParser.getPriceInTextFormat(searchString, html).replace(",","."))
finalPriceValueTemp = (prxResultParser.getPriceInTextFormat(searchString, html))
print(finalPriceValueTemp)

finalPriceValue = (prxResultParser.getPriceInTextFormat("<b>", finalPriceValueTemp))
print(finalPriceValue)



'''
textToSearchFor = "CIEL3"
searchString = "BVMF: " + textToSearchFor

parser = MyHTMLParser()
parser.feed(html)
'''

