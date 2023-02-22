"Filtro Montana rusa"


def pasa_o_no(ed, es):
    if ed > 14 and es > 1.62:
        return True
    else:
        return False


edad = int(input("Pon tu edad: "))
estatura = float(input("Pon tu estatura: "))

if pasa_o_no(edad, estatura):
    print("Pasa")
else:
    print("No pasa")
