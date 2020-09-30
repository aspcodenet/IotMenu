
def SubMenu1():
    b = 555
    while True:
        print("SUB")
        print("1. Hej")
        print("2. Hopp")
        print("3. Avsluta")
        i = int(input("Välj:"))
        if i == 1:
            print("Hej valdes")
        elif i == 2:
            print("Hopp valdes")
        elif i == 3:
            break
        else:
            print("Skriv in ett tal mellan 1 och 3 dummer")



def HuvudMeny():
    a = 123
    while True:
        print("Huvud")
        print("1. Sub")
        print("2. Avsluta")
        i = int(input("Välj:"))
        if i == 1:
            SubMenu1()
        if i == 2:
            break
    
def SafeInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("mata in ett tal")

antalApples = SafeInput("mata in antal äpplen")
antal = SafeInput("mata in antal personer")
try:
    print(f"Alla får {antalApples/antal} äpplen var")
except:
    print("Oj vad konstigt det blev")


print("Start")
i = 12
HuvudMeny()
print("sdasasda")