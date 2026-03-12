#Heladeria factura de varios clientes
print("Bienvenido a heladería mil sabores")
print("opción a ejecutar: \n" \
"1.Tomar orden.\n" \
"2.Salir ")
while opcion != "2":
    opcion =input("opción a ejecutar: \n" \
"1.Tomar orden.\n" \
"2.Salir ")
    if opcion == "1":
        producto = input("Seleccione el producto:\n" \
        "1.cono ...3000\n" \
        "2.vaso ...4000\n" \
        "3.banana split")
