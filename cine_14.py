#Cine control de sala
niños = 0
adultos = 0
adultos_m = 0
total_personas = 0
entradas = 0

capacidad = int(input("ingrese el número de capacidad de la sala de cien: "))

opcion = ""

while opcion != "2" and entradas < capacidad:
    opcion = input("Elije la opción que deseas: \n" \
                    "1.Registrar usuario\n" \
                    "2.Terminar usuarios en la sala: ")  
    
    if  opcion  == "2":
        break

    elif opcion == "1":
        edad = int(input("Ingresar edad del usuario: "))

        if  4 < edad <=17:
            niños += 1
            total_personas +=1
            entradas += 1

        elif edad <= 59:
            adultos += 1
            total_personas += 1
            entradas += 1

        elif edad <= 120:
            adultos_m += 1
            total_personas += 1
            entradas += 1
        
        else:
            print("dato erroneo")
    else: 
        print("Opción no valida, escoga una opción entre 1 y 2")

print("DETALLES DE LA FUNCIÓN")
if entradas == capacidad:
    print("Sala llena")
else:
    print("La Sala no se llenó")
print(f"Total de personas: {total_personas}")
print(f"Cantidad de niños: {niños}")
print(f"cantidad de adutltos: {adultos}")
print(f"Cantidad de adultos mayores: {adultos_m}")


        
    


                           