#Heladeria factura de varios clientes
print("Bienvenido a heladería mil sabores")
clientes = 0

total_cono = 0
total_vasos = 0
total_banana = 0
valor = 0
total_vendido = 0
cantidad = 0
opcion = ""
while opcion != "2":
    opcion =input("opción a ejecutar: \n" \
"1.Tomar orden.\n" \
"2.Salir:  ")
    total_vendido += valor
    if opcion == "1":
        producto = input("Seleccione el producto:\n" \
        "1.cono ...3000\n" \
        "2.vaso ...4000\n" \
        "3.banana split ...9000: ")

        cantidad = int(input("Seleccionar cantidad del producto: "))

        clientes += 1
        
        if producto == "1":          
            valor = cantidad * 3000
            print(f"Total a pagar es de {valor}")
            total_cono += cantidad
        elif producto == "2":         
            valor = cantidad * 4000
            print(f"Total a pagar es de {valor}")
            total_vasos += cantidad
        elif producto == "3":
            valor = cantidad * 9000
            print(f"Total a pagar es de {valor}")
            total_banana += cantidad
        else: 
            print("Opción no valida")
    

print("Resumen de ventas")
print(f"Número de clientes: {clientes}")
print(f"Total vendido: {total_vendido}")

if total_cono > total_vasos and total_cono > total_banana:
    print("El cono fue el producto mas vendido")
elif total_vasos > total_cono and total_vasos > total_banana:
    print("Los vasos fue el producto mas vendido ")
else:
    print("Banana split fue el producto más vendido")