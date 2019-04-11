
aList = list()
def addNumberToList(num):
    aList.append(num)
def main():
    num1 = int (input("give me a number!"));
    while(num1 != 0):
        addNumberToList(num1)
        num1 = int (input("give me a number!"));
    
    finalString = "" 
    for x in aList:
       finalString += str(x) + ", "
    
    print(finalString)   


main();
