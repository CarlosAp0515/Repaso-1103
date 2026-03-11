print("BIENVENID@ A JUAN VALDEZ ;)")

bebida = input("Selecciona la bebida que desee comprar.\n" \
"1. Café ...4000\n" \
"2. Té ...3500\n" \
"3. Jugo ...5000\n" \
": ")
cantidad = int(input("Que cantidad de este producto desea llevar: "))

if cantidad <= 0:
    print("Cantidad no valida")
elif bebida == "1":
    precio = 4000 * cantidad
    print("Detalles de la compra: \n" \
    "Producto: Café\n" \
    "Precio: 4000\n" 
    f"cantidad: {cantidad}""\n"
    f"precio total: {precio}")

elif bebida == "2":
    precio = 3500 * cantidad
    print("Detalles de la compra: \n" \
    "Producto: Té\n" \
    "Precio: 3500\n" 
    f"cantidad: {cantidad}""\n"
    f"precio total: {precio}")

elif bebida == "3":
    precio = 5000 * cantidad
    print("Detalles de la compra: \n" \
    "Producto: Té\n" \
    "Precio: 3500\n" 
    f"cantidad: {cantidad}""\n"
    f"precio total: {precio}")
else:
    print("opción invalida")





  


