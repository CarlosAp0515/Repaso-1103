n = 5
print("bIENVENIDO A HELADERIA MUNDO SABOR")

sabores = []
i = 0
for i in range(n):
    print("bIENVENIDO A HELADERIA MUNDO SABOR")
    pedido = input("Eliga el sabor de helado que desea escoger: .\n" \
    "1.Vainilla\n" \
    "2.Chocolate\n" \
    "3.Fresa." "\n"
    ": ")
    if pedido == "1":
        print("Sabor vainilla seleccionado")
        sabores.append("Vainilla")

    elif pedido== "2":
        print("Sabor chocolate seleccionado")
        sabores.append("Chocolate")
    elif pedido == "3":
        print("Sabor fresa seleccionado")
        sabores.append("Fresa")
    else:
        print("Opción invalida")

print("Sabores seleccionados:")
print(sabores)