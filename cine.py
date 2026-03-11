print("BIENVENDIO A PELIMOVIE CINEMAFILMS")
edad = int(input("Para saber el valor de su entrada por favor digite su edad: "))
if 0 < edad < 12:
    print("Para menores de 12 años el precio de la boleta es de 8000")
elif 12 < edad < 60:
    print(f"su edad es de:{edad} , El precio de su boleta es de 12000")
elif edad > 60:
    print(F"Para mayores de 60 años el precio de la boleta es de 9000")
else:
    print("opción invalida")
    