def mostrar_menu():
    print("========== MENÚ PRINCIPAL ===========")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion = int(input("Ingrese una opción (1-6): "))
        if 1 <= opcion <= 6:
            return opcion
        print("Opción inválida. Ingrese un número entre 1 y 6.")

def agregar_paciente(pacientes):
    nombre = input("Ingrese el nombre del paciente: ")
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío.")
        return
    edadT = input("Ingrese la edad del paciente: ")
    edad_valida, edad = validar_edad(edadT)
    if not edad_valida:
        print("Error: la edad debe ser un número entero mayor que cero.")
        return
    tempT = input("Ingrese la temperatura del paciente: ")
    temp_valida, temperatura = validar_temperatura(tempT)
    if not temp_valida:
        print("Error: la temperatura debe ser un número entre 35.0 y 42.0.")
        return
    paciente = {
        "nombre": nombre.strip(),
        "edad": edad,
        "temperatura": temperatura,
        "atendido": False,
    }
    pacientes.append(paciente)
    print("Paciente agregado correctamente.")
    
def validar_nombre(nombre):
    return len(nombre.strip()) > 0


def validar_edad(edadT):
    if not edadT.isdigit():
        return False, None
    edad = int(edadT)
    return edad > 0, edad

def validar_temperatura(tempT):
    try:
        temperatura = float(tempT)
    except ValueError:
        return False, None
    return 35.0 <= temperatura <= 42.0, temperatura

def buscar_paciente(pacientes, nombre_buscar):
    for indice, paciente in enumerate(pacientes):
        if paciente["nombre"] == nombre_buscar:
            return indice
    return -1

def actualizar_estado(pacientes):
    for paciente in pacientes:
        paciente["atendido"] = paciente["temperatura"] <= 37.0

def mostrar_pacientes(pacientes):
    actualizar_estado(pacientes)
    print("******** LISTA DE PACIENTES ********")
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    for paciente in pacientes:
        print()
        print(f"Nombre: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Temperatura: {paciente['temperatura']}")
        estado = "ATENDIDO" if paciente["atendido"] else "REQUIERE ATENCION"
        print(f"Estado: {estado}")
        print("********************************************")

def main():
    pacientes = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_paciente(pacientes)
        elif opcion == 2:
            nombre = input("Ingrese el nombre a buscar: ")
            posicion = buscar_paciente(pacientes, nombre)
            if posicion == -1:
                print("No se encontró ningún paciente con ese nombre.")
            else:
                paciente = pacientes[posicion]
                print(f"Paciente encontrado en la posición {posicion}:")
                print(f"Nombre: {paciente['nombre']}")
                print(f"Edad: {paciente['edad']}")
                print(f"Temperatura: {paciente['temperatura']}")
                print(f"Atendido: {paciente['atendido']}")
        elif opcion == 3:
            nombre = input("Ingrese el nombre del paciente a eliminar: ")
            posicion = buscar_paciente(pacientes, nombre)
            if posicion == -1:
                print(f"El paciente '{nombre}' no se encuentra registrado.")
            else:
                pacientes.pop(posicion)
                print("Paciente eliminado correctamente.")
        elif opcion == 4:
            actualizar_estado(pacientes)
            print("Estado de los pacientes actualizado.")
        elif opcion == 5:
            mostrar_pacientes(pacientes)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break

if __name__ == "__main__":
    main()