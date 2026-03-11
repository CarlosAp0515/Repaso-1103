#ignacio
print("Bienvenido a fitgym")

edad = int(input("Para saber a que clase puede pertenecer, porfavor ingrese su edad: "))

if edad < 13:
    print("Usted es menor de 13 años, no puede ingresar al gimnasio.")

elif edad >= 13 and edad <= 17:
    print("Usted puede ingresar a la clase Juvenil")
elif  18 <= edad <= 59:
    print("Edad idonea para ingresar a clase genreal")
elif edad >= 60:
    print("Usted puede unirse a la clase senior")
else: 
    print("Digite una opción valida")
 