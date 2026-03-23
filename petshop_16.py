n = 10
total_alimento = 0
total_juguetes = 0
total_acc = 0

for i in range(n):
    categoria = input("Ingrese la categoria del producto(alimento, juguetes, accesorios): ")
    if categoria == "alimento":
        precio = int(input("Ingrese el valor de la compra: "))
        total_alimento += precio
    elif categoria == "juguetes":
        precio = int(input("Ingrese el valor de la compra: "))
        total_juguetes += precio
    elif categoria == "accesorios":
        precio = int(input("Ingrese el valor de la compra: "))
        total_acc += precio
    else:
        print("Categoria no valida")
print("resumen de ventas")
print(f"Total alimento: {total_alimento}")  
print(f"Total juguetes: {total_juguetes}")  
print(f"Total accesorios: {total_acc}")
if total_alimento > total_juguetes and total_alimento > total_acc:
    print("Categoria mas vendida: Alimento")
elif total_juguetes > total_alimento and total_juguetes > total_acc:
    print("Categoria mas vendida: Juguetes")
else:
    print("Categoria mas vendida: Accesorios")
    