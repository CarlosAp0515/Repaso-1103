#GYM QUE REGISTRA PROMEDIO DE RENDIMIENTO PERSONAL

usuarios = 0
low = 0
medium = 0
high = 0
while usuarios <6:

    nombre = input("Ingrese su nombre: ")
    dias = int(input("Ingrese el número de dias asistidos a la semana: "))
    minutos = int(input("Ingrese el numero de minutos que entreno en promedio: "))

    if dias < 0 or dias > 7:
        print("Número de días inválido")
        continue

    if dias < 3: 
        print(f"Hola {nombre}, se te ha asignado en la categoria BAJO COMPROMISO ")
        low += 1

    elif dias <= 4:
        print(f"Hola {nombre}, se te ha asignado en la categoria COMPROMISO MEDIO ")
        medium += 1

    else:
        print(f"Hola {nombre}, se te ha asignado en la categoria COMPROMISO ALTO ")
        high += 1
    
    usuarios += 1

print("Resumen")
print(F"Número de personas en BAJO COMPROMISO: {low} ")
print(f"Número de personas en COMPROMISO MEDIO: {medium}")
print(f"Número de personas en COMPROMISO ALTO: {high}")





 