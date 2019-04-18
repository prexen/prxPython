
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


#pede inputs e mostra o menor deles ate ambos os numero serem iguais.
def questao1():
    programRunning = True;
    while(programRunning):
        num1 = float (input("first real number!..."));
        num2 = float (input("second real number..."));
        if(num1 < num2):
            print("menor numero é: " , num1)
        elif(num1 > num2):
            print("menor numero é: " , num2)
        elif(num1 == num2):
            print("end program.")
            programRunning = False;
