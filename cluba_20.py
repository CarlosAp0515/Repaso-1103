basico = 50000
premiun = 90000
familiar = 130000

total_recaudado = 0
total_basico = 0
total_premiun = 0
total_familiar = 0
plan_mas_vendido = 0
opcion = ""

while opcion != "2":
    opcion = input("Elije la opcion que deseas:\n"
                   "1.Registrar persona\n" 
                   "2.salir: " )

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        edad = int(input("Ingrese la edad del cliente: "))
        plan = input("Ingrese el tipo de plan que deseas: \n" \
                          "1.Básico\n" \
                          "2.Premiun\n" \
                          "3.Familiar: ")
        if plan == "1":
            total_basico += 1
            total_recaudado += basico
            if edad < 18:
                print("Registro juvenil")
            elif edad > 59:
                print("Beneficio senior")

        elif plan == "2":
            total_premiun += 1
            total_recaudado += premiun
            if edad < 18:
                print("Registro juvenil")
            elif edad > 59:
                print("Beneficio senior")

        elif plan == "3":
            total_familiar += 1
            total_recaudado += familiar
            if edad < 18:
                print("Registro juvenil")
            elif edad > 59:
                print("Beneficio senior")

        else:
            print("Opcion no valida")

        if total_basico > total_premiun and total_basico > total_familiar:
            plan_mas_vendido = "Básico"
        elif total_premiun > total_basico and total_premiun > total_familiar:
            plan_mas_vendido = "Premiun"
        else:
            plan_mas_vendido = "Familiar"

    elif opcion == "2":
        break

print("\nRESULTADOS")
print(f"El plan mas vendido es: {plan_mas_vendido}")
print(f"El total recaudado es: {total_recaudado}")
print(f"El total de clientes basico es: {total_basico}")
print(f"El total de clientes premiun es: {total_premiun}")
print(f"El total de clientes familiar es: {total_familiar}")