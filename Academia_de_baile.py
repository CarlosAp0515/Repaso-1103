#ACADEMIA DE BAILE QUE  REGISTRA ASISTENCIA A LAS CLASES EN UN MES
print("Bienvenido a nuestra academia de baile")
clases = int(input("Ingrese el número de clases a las  que asitiste este mes: "))

if 0<clases<5:
    print("Asistencia baja")
elif  5>clases>8:
    print("Asistencia media")
elif clases>= 9:
    print("Asistencia alta")
else:
    print("????")

