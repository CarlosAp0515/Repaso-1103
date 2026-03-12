#Parqueadero de cobros por hora
print("BIENVENIDO A PARQUEADERO APARCAMELO AHÍ")
print("Nuestro servicio consiste en que la primera hora te cuesta 5000$, cada hora adicional son 3000$")
tiempo = int(input("Cuanto tiempo deseas tener aparcado tu auto (Ingresa el número de horas): "))

if tiempo <= 0:
    print("El tiempo es de una hora en adelante")
elif tiempo == 1:
    print("El valor a pagar es de 5000")
elif 24 > tiempo > 1:
    valor  = 5000 + ((tiempo - 1) * 3000)
    print(f"El total del valor a pagar del parqueo es de: {valor}")
else:
    print("tiempo no valido")
