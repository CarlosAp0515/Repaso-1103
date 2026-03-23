n = 7
total_dia = 0
total_corte = 0
total_cepillado = 0
total_tintura = 0

for i in range(n):
    print("Registro del clientes")
    nombre = input("Ingrese el nombre del cliente: ")
    tipo = input("Tipo de servicio (corte, cepillado, tintura): ")
    valor = float(input("Ingrese el valor del servicio: "))

    if tipo == "corte":
        total_dia += valor
        total_corte += 1

    elif tipo == "cepillado":
        total_dia += valor
        total_cepillado += 1

    elif tipo == "tintura":
        total_dia += valor
        total_tintura += 1

    else:
        print("Tipo de servicio no valido")

print("\nRESULTADOS")
print(f"Total del dia: {total_dia}")
print(f"Total de clientes en corte: {total_corte}")
print(f"Total de clientes en cepillado: {total_cepillado}")
print(f"Total de clientes en tintura: {total_tintura}")

if total_corte > total_cepillado and total_corte > total_tintura:
    print("Tipo de servicio mas solicitado: Corte")
elif total_cepillado > total_corte and total_cepillado > total_tintura:
    print("Tipo de servicio mas solicitado: Cepillado")
else:
    print("Tipo de servicio mas solicitado: Tintura")