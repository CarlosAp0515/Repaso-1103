def resultado(nombre, promedio):
    if promedio < 60:
        print(f"El promedio de {nombre} es: {promedio}")
        print(f"Su nivel es bajo")
    elif 60 <= promedio < 80:
        print(f"El promedio de {nombre} es: {promedio}")
        print(f"Su nivel es medio")
    else:
        print(f"El promedio de {nombre} es: {promedio}")
        print(f"Su nivel es alto")
        return

promedios_estudiantes = 0
bajo = 0
medio = 0
alto = 0
estudiantes = 0
promedio_mas_alto = 0
nombre_del_estudiante_mas_alto = ""
opcion = ""
while opcion != "2":
    opcion = input("Elije la opcion que deseas: \n" \
                    "1.Registrar nota estudiante\n" \
                    "2.salir: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        nota_s = float(input("Ingrese la nota del speaking: "))
        nota_l = float(input("Ingrese la nota del listening: "))
        nota_r = float(input("Ingrese la nota del reading: "))
        promedio = (nota_s + nota_l + nota_r) / 3
        estudiantes += 1
        promedios_estudiantes += promedio

        if promedio < 60:
            bajo += 1
        elif 60 <= promedio < 80:
            medio += 1
        else:
            alto += 1

        resultado(nombre, promedio) 

        if promedio > promedio_mas_alto:
            promedio_mas_alto = promedio
            nombre_del_estudiante_mas_alto = nombre

    elif opcion == "2":
        break

print(f"El promedio de los estudiantes es: {promedios_estudiantes / estudiantes}")
print(f"El numero de estudiantes con bajo es: {bajo}")
print(f"El numero de estudiantes con medio es: {medio}")
print(f"El numero de estudiantes con alto es: {alto}")
print(f"El promedio mas alto es de {promedio_mas_alto} y pertenece al estudiante {nombre_del_estudiante_mas_alto}")
