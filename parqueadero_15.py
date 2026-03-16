total_recaudado = 0
carros = 0
motos = 0

mayor_pago = 0
placa_mayor = ""

for i in range(8):

    print("Registro del vehículo", i+1)

    placa = input("Ingrese la placa: ")
    tipo = input("Tipo de vehículo (carro/moto): ")
    horas = int(input("Horas parqueado: "))

    if tipo == "carro":
        pago = horas * 4000
        carros += 1

    else:
        pago = horas * 2000
        motos += 1

    total_recaudado += pago

    if pago > mayor_pago:
        mayor_pago = pago
        placa_mayor = placa

print("\nRESULTADOS")
print("Total recaudado:", total_recaudado)
print("Cantidad de carros:", carros)
print("Cantidad de motos:", motos)
print("Vehículo que pagó más:", placa_mayor, "con", mayor_pago)