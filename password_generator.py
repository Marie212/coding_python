import random
def contras(): 
    letter = "abcdefghijklmnopqrstuvwxyz"
    mayusc = letter.upper()
    number = "0123456789"

    passw1= random.choice(letter)
    passw2= random.choice(mayusc)
    passw3= random.choice(number)
    passw4 = passw1 + passw2+ passw3
    passw6 = ""
    passw = letter + mayusc + number
    limit = random.randint(6, 13)

    for i in range(0, limit):
        passw5= random.choice(passw)
        passw6 = passw6 + passw5  
    codigo = passw6 + passw4
    return codigo

def menus():
    print("MENU\n1. Generar codigo\n2. obtener codigo\n3. salir")
    opc = input("Ingrese una opcion: ")
    return opc
cuentas = []
while True:
    opcion = menus()
    if opcion == "1":
        cuenta = input("ingrese la cuenta para la cual quiere generar codigo: ")
        x = cuenta
        y = contras()
        dic = {
            'cuen': x,
            'contras': y
        }
        cuentas.append({'cuent': x, 'contras': y})
        print(cuentas)
    if opcion == "2":
            print(cuentas)
            for c in cuentas:
                buscar = input("ingrese la cuenta de la cual quiere ver la contraseña: ")
                if buscar == c['cuent']:
                    print('tu password de ' + buscar + ' es: ', c['contras'])
    if opcion == "3":
        break