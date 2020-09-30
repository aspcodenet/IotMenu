#Vända på if -> mindre nästling

def createAccount():
    while True:
        kontonummer=input("Ange Nytt kontonummer ->")
        if not checkDigit(kontonummer):
            cprint("Ange rätt ny nummer !","red")
            continue

        kontolist = readFile()
        existed=False
        if getKonto(kontonummer,kontolist): 
            cprint("Account is already existed !","red")
            existed=True          
        if not existed:
            today=datetime.datetime.now()
            todayStr= today.strftime("%Y-%m-%d, %H:%M:%S")
            kontoObj=Konto(todayStr,kontonummer,[{"dateinfo":todayStr, "ut":0, "in":0}])
            kontolist.append(kontoObj)
            writeToFile(kontolist)
            return True
