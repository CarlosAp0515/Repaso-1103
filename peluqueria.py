#Peluqueria ejercicio 7
print("BIENVENIDO A PELUQUERIA EL PELUCON")
turno = int(input("Porfavor ingrese la hora en que desee apartar su turno, (debe ingresar el número dela hora entre 0 a 23): "))

if   6 <= turno <= 11:
    print("Has apartado en el turno de mañana")

elif  12<= turno <=17:
    print("Has apartado en el turno de tarde")

elif 18<= turno <=22:
    print("Has apartado turno en la noche")
else:
    print("Fuera de horario")
