#Heladeria factura de varios clientes
print("Bienvenido a heladería mil sabores")

clientes = 0
total_cono = 0
total_vasos = 0
total_banana = 0
total_vendido = 0

opcion = ""

while opcion != "2":

    opcion =input("opción a ejecutar: \n" \
"1.Tomar orden.\n" \
"2.Salir:  ")
    
    
    if opcion == "1":

        valor = 0
        
        producto = input("Seleccione el producto:\n" \
        "1.cono ...3000\n" \
        "2.vaso ...4000\n" \
        "3.banana split ...9000: ")

        cantidad = int(input("Seleccionar cantidad del producto: "))
        
        if producto == "1":          
            valor = cantidad * 3000
            total_cono += cantidad
            clientes += 1

        elif producto == "2":         
            valor = cantidad * 4000          
            total_vasos += cantidad
            clientes += 1

        elif producto == "3":
            valor = cantidad * 9000            
            total_banana += cantidad
            clientes += 1

        else: 
            print("Opción no valida")
        
        total_vendido += valor
        print(f"Total a pagar: {valor}")

    

print("Resumen de ventas")
print(f"Número de clientes: {clientes}")
print(f"Conos vendidos: {total_cono}")
print(f"Vasos vendidos: {total_vasos}")
print(f"Banana split vendidos: {total_banana}")
print(f"Total vendido: {total_vendido}")

if total_cono > total_vasos and total_cono > total_banana:
    print("El producto más vendido fue: Cono")

elif total_vasos > total_cono and total_vasos > total_banana:
    print("El producto más vendido fue: Vaso")

elif total_banana > total_cono and total_banana > total_vasos:
    print("El producto más vendido fue: Banana Split")

else:
    print("Hubo un empate entre los productos más vendidos")