import datetime

"Fecha de nacimiento y generacion"


def edad_actual(nacimiento):
    anio = int(datetime.date.today().strftime("%Y"))
    mes = int(datetime.date.today().strftime("%m"))
    dia = int(datetime.date.today().strftime("%d"))
    edad_persona = anio - int(nacimiento[2])
    if mes >= int(nacimiento[1]) and dia >= int(nacimiento[0]):
        print(f"Tienes {edad_persona} años")
        print(f"Ya cumpliste años este año")
    else:
        print(f"Tienes {edad_persona - 1} años")
        print(f"No has cumplido años este año")


def generacion(nacimiento):
    if int(nacimiento[2]) >= 1920 and int(nacimiento[2]) <= 1939:
        print("Generacion sileciosa")
    elif int(nacimiento[2]) >= 1940 and int(nacimiento[2]) <= 1959:
        print("Baby boomers")
    elif int(nacimiento[2]) >= 1960 and int(nacimiento[2]) <= 1979:
        print("Generacion X")
    elif int(nacimiento[2]) >= 1980 and int(nacimiento[2]) <= 1989:
        print("Generacion Y o millenials")
    else:
        print("Generacion Z")


fecha_de_nacimiento = input('Dame tu fecha de nacimiento (dd/mm/aaaa): ').split('/')
edad_actual(fecha_de_nacimiento)
generacion(fecha_de_nacimiento)
