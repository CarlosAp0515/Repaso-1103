#contar productos caros
contador = 0
i = 0
print("Bienvenido a  mundo deportivo, un placer verte por aqui")
for i in range(6):
    valor =int(input("Digite el precio del producto: "))
    if valor >100000:
        contador += 1

print(f"La cantidad de productos que cuestan más de 100.000$ es de: {contador}")



