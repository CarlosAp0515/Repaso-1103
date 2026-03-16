#GYM QUE REGISTRA PROMEDIO DE RENDIMIENTO PERSONAL

usuarios = 0
low = 0
medium = 0
high = 0
while usuarios <6:
    nombre = input("Ingrese su nombre: ")
    dias = int(input("Ingrese el número de dias asistidos a la semana: "))
    minutos = int(input("Ingrese el numero de minutos que entreno en promedio: "))
    if 0 <= dias < 3: 
        print(f"Hola {nombre}, se te ha asignado en la categoria BAJO COMPROMISO ")
        usuarios += 1
        low += 1
    elif  3 <= dias <= 4:
        print(f"Hola {nombre}, se te ha asignado en la categoria COMPROMISO MEDIO ")
        usuarios += 1
        medium += 1
    elif 7 >= dias >= 5:
        print(f"Hola {nombre}, se te ha asignado en la categoria COMPROMISO ALTO ")
        usuarios += 1
        high += 1
    else:
        print("número de dias invalidos")

print("Resumen")
print(F"Número de personas en BAJO COMPROMISO: {low} ")
print(f"Número de personas en COMPROMISO MEDIO: {medium}")
print(f"Número de personas en COMPROMISO ALTO: {high}")





 