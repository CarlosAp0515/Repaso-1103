#Cafeteria con descuento según consumo
cafe = 4000
capuchino = 7000
pastel = 6000

total_vendido = 0
total_cafe = 0
total_capuchino = 0
total_pastel = 0
descuentos = 0

pedido = ""

while pedido != "salir":
    pedido = input("cafeteria cofi el cafetro, \n" \
    "Oprima ENTER para registrar pedido\n" \
    "Escriba (salir) para finalizar: ")
    if pedido == "salir":
        break
    valor = 0

    producto = input("Producto seleccionado: \n" \
        "1. café\n" \
        "2. capuchino\n" \
        "3. pastel\n" \
        "(elija la opcion del 1 al 3): ")
    
    cantidad = int(input("Escribir el número de la cantidad del producto: "))

    if producto == "1":
            valor = cafe * cantidad
            total_cafe += cantidad
            nombre = "café"

    elif producto == "2":
            valor = capuchino * cantidad
            total_capuchino += cantidad
            nombre = "capuchino"

    elif producto == "3":
            valor = pastel * cantidad
            total_pastel += cantidad
            nombre = "pastel"
        
    else:
            print("Opción invalida")
            continue
    
    if valor > 20000:
        valor -= valor * 0.10
        descuentos += 1

    print("\nResumen de compra")
    print(f"Producto: {nombre}")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: {valor}")

    total_vendido += valor

print("TOTAL DEL DIA")
print(f"Total vendido: {total_vendido}")
print(f"cafes vendidos: {total_cafe}")
print(f"capuchinos vendidos: {total_capuchino}")
print(f"pasteles vendidos: {total_pastel}")
print(f"Descuentos aplicados: {descuentos}")




    


