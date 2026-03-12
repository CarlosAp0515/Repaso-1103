#Tienda de mascotas: alimento por tipo de comida
print("Bienvenido a mundomascota")
print("Recomendación de alimentos para tu mascota")
mascota = input("Sobre que tipo de mascota quieres asesoramiento para su alimentación (escribir todo en minuscula): ")

if mascota == "perro":
    print("Para los perros es recomendable concentrado para perro según su edad y peso, tambien diferente tipos de proteinas.")
elif mascota == "gato":
    print("Para una buena alimentación de su gato es recomendable que consuman concentrado para gatos previamene avalados y alimentos blandos para gatos de disitintos sabores")
elif mascota == "conejo":
    print("Para los conejos es recomendable que su alimentación se base en zanahorias y otros tipos diferentes de verduras y frutas")
else:
    print("No se encuentra en la base de datos")
    