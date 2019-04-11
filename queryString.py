

#/query?function=GLOBAL_QUOTE&symbol=CIEL3.SA&apikey=3G50AKKPMVDXHTCL&datatype=json
#/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22

#def addRoute():


path = "/query?func=GET_PRICE&ticket=CIEL3&apikey=478GJH4890gjkflwsd9234da&datatype=json"


pathFunction = path.strip("/")#tira o / do comeco
pathFunction = pathFunction.split("?")
print(pathFunction[0])#/query

argumentos = pathFunction[1].split("&")
print(argumentos)

#o 0 ali eh o func=GET_PRICE
#o 1 ali eh o ticket=CIEL3.SA
#o 2 ali eh o apikey=478GJH4890gjkflwsd9234da
#o 3 ali eh o datatype=json

#print(argumentos[0].split("=")[1])#retorna GET_PRICE #o 0 ali eh o func=GET_PRICE

if(argumentos[0].split("=")[1] == "GET_PRICE"):
    print("ACHEI o q  eu queria")

'''
#print(len(argumentos))
for x in argumentos:
    print(x.split("=")[0])
    print(x.split("=")[1])
'''