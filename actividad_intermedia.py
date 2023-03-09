def getcurso():
    loop = True
    curso = dict()
    curso["nombre"] = input("Ingresa el nombre del curso: ")
    curso["cantidad"] = int(input("Cuantos alumnos tiene el curso: "))
    while loop:
        curso["estado"] = input("Agrega un estado de los siguientes Activo || Finalizado || En curso: ")
        for x in ESTADOS:
            if x == curso["estado"]:
                loop = False
                break
        else:
            print("Opcion erronea")
    curso["clases"] = int(input("Ingresa el numero de clases que tendra el curso: "))
    return curso
def modcurso(academy):
    for lop in academy:
        print(lop["nombre"])
    nombre_del_curso = input("Que curso quiere modificar ")
    for i in ESTADOS:
        print(i)
    estado = input("Cual es el estado al que vas a mover el curso: ")
    for index, lop in enumerate(academy):
        if lop["nombre"] == nombre_del_curso:
            academia[index]["estado"] = estado
def consulta(academy):
    for lop in academy:
        print(lop["nombre"])
    curs = input("Cual de los cursos anteriores quiere consulta: ")
    for i in academy:
        if i["nombre"] == curs:
            imprimirformatoconsulta(i)
            break
    else:
        print("Curso mal escrito o inexistente")
def imprimirformatoconsulta(dic):
    print(f"{dic['nombre']}----------------------------------------------------------------")
    print(f"Numero de alumnos: {dic['cantidad']}")
    print(f"Estado de curso: {dic['estado']}")
    print(f"Numero de clases: {dic['clases']}")

ESTADOS = ("Activo", "En curso", "Finalizado")
OPCIONES = ("Alta", "Modificar estado", "Consulta especifica", "Consulta general")

academia = []
while True:
    print("MENU--------------------------------------------------")
    for i in OPCIONES:
        print(i)
    opcion = input("Escribe la accion completa: ")
    if opcion == OPCIONES[0]:
        academia.append(getcurso())
    elif opcion == OPCIONES[1]:
        modcurso(academia)
    elif opcion == OPCIONES[2]:
        consulta(academia)
    elif opcion == OPCIONES[3]:
        for c in academia:
            imprimirformatoconsulta(c)
            input("Press enter para continuar")
    else:
        print("Opcion incorrecta vuelve a intentar")
        input("Press enter para continuar")

