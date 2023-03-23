import random


class participante:
    def __init__(self, nombre, email, puntos, raza, partidas, estado):
        self.nombre = nombre
        self.puntos = puntos
        self.email = email
        self.raza = raza
        self.partidas = partidas
        self.estado = estado

    def ganador(self):
        self.puntos += 3
        self.partidas += 1

    def perdedor(self):
        self.puntos += 1
        self.estado = "Inactivo"
        self.partidas += 1

    def __repr__(self):
        return(f"Nombre: {self.nombre}, Email: {self.email}, Puntos: {self.puntos}, Raza: {self.raza}, Partidas: {self.partidas}")

"""Funciones"""
def nuevoparticipante():
    nombre = input("Ingresa el nombre del participante: ")
    email = input("Ingresa el email del participante: ")
    imprimir_lista(RAZA)
    razain = True
    while razain:
        raza = input("Ingresa una raza de las anteriores: ")
        if raza in RAZA:
            razain = False
    nuevo_registro = participante(nombre, email, 0, raza, 0, "Activo")
    return nuevo_registro
def imprimir_lista(lista):
    print("-".join(lista))
def torneo():
    jugador1 = random.randint(0, len(participantes) - 1)
    jugador2 = random.randint(0, len(participantes) - 1)
    ganador = random.randint(0, 2)
    while jugador1 == jugador2:
        jugador2 = random.randint(0, len(participantes) - 1)
    if participantes[jugador1].partidas == participantes[jugador2].partidas:
        print(f"{participantes[jugador1].nombre} vs {participantes[jugador2].nombre}")
        if ganador == 0:
            print(f"El ganador es {participantes[jugador1].nombre}")
            participantes[jugador1].ganador()
            participantes[jugador2].perdedor()
            participantesinactivos.append(participantes[jugador2])
            participantes.pop(jugador2)
        else:
            print(f"El ganador es {participantes[jugador2].nombre}")
            participantes[jugador2].ganador()
            participantes[jugador1].perdedor()
            participantesinactivos.append(participantes[jugador1])
            participantes.pop(jugador1)
    else:
        torneo()

"""Variable globales"""
RAZA = ("Terran", "Zerg", "Protoss")
participantes = []
participantesinactivos = []
OPCIONES = ("Añadir un jugador", "Empezar torneo")
menu = True

"""Main"""
while menu:
    print("MENU " + "-" * 80 )
    imprimir_lista(OPCIONES)
    opcion = input("Elige una opcion: ")
    if opcion == OPCIONES[0]:
        participantes.append(nuevoparticipante())
    elif opcion == OPCIONES[1]:
        if len(participantes) % 2 == 0:
            menu = False
        else:
            print("Necesitas añadir a otro participante para empezar el torneo")
    else:
        print("Elige una opcion valida")
while len(participantes) != 1:
    torneo()
print(f"El ganador del torneo es {participantes[0].nombre} con {participantes[0].puntos} puntos")
participantes[0].estado = "Inactivo"
participantesinactivos.append(participantes[0])
guardar = input("Deseas guardar la informacion en un archivo? (S/N): ")
if guardar == "S":
    with open("Puntuacion", "w") as file:
        file.write("Torneo" + "-"*80 + "\n")
        for jugador in reversed(participantesinactivos):
            file.write(f"{jugador.__repr__()}\n")
else:
    print("Fin de la partida")