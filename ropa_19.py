n = 10
t_agotado = 0
t_stock_bajo = 0
t_stock_normal = 0

for i in range(0,n,1):
    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese la cantidad disponible del producto: "))
    if stock == 0:
        t_agotado += 1
    elif 1 <= stock < 6:
        t_stock_bajo += 1
    else:
        t_stock_normal += 1

print("\RESUMEN DE LISTADO DE PRODUCTOS")
print(f"Productos agotados: {t_agotado}")
print(f"Productos con stock bajo: {t_stock_bajo}")
print(f"Productos con stock normal: {t_stock_normal}")