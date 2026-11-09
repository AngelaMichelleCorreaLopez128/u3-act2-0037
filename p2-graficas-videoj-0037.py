
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Angela Correa NC = 0037
#crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de videojuegos con 4 elementos por lista
mc  = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]

# Creamos una lista de listas (conformando la tabla)
lista_juegos=[mc, gta, tet, wii, pub]
#print(lista_juegos)

# Utilizar panda para organizar la tabla (dataframe o marco de datos)
# A cada columna le ponemos nombre
df_juegos=pd.DataFrame(lista_juegos,columns=["Nombre","Cantidad","Es_multijugador","Año"])
print(df_juegos)

# creamos el archivo CSV y lo guardamos en CSV
# df_juegos.to_csv("juegos.csv", index=False)

# crear grafica de lineas
# donde x es Nombre en el eje horizontal
# donde y es Cantidad en el eje vertical
plt.plot(df_juegos["Nombre"], df_juegos["Cantidad"])
plt.title("Grafica de videojuegos 0037")
plt.xlabel("Nombre de los videojuegos")
plt.ylabel("Copias vendidas en millones")
plt.show()

# Creamos una grafica de puntos
plt.scatter(df_juegos["Nombre"], df_juegos["Cantidad"])
plt.show()

# Grafica de barras
plt.bar(df_juegos["Nombre"], df_juegos["Cantidad"])

# Etiquetas y titulos
plt.title("Videojuegos 0037")
plt.xlabel("Los videojuegos")
plt.ylabel("Copias vendidas en millones")

# Mostrar el gráfico
plt.show()

# Ordenar la grafica de barras de manera descendente
# De la mas grande a la pequeña
df_j_ordenar=df_juegos.sort_values(["Cantidad"],ascending=False)
plt.bar(df_j_ordenar["Nombre"], df_j_ordenar["Cantidad"])
plt.show()

# Coloreando la grafica
df_j_ordenar=df_juegos.sort_values(["Cantidad"],ascending=False)
plt.bar(df_j_ordenar["Nombre"], df_j_ordenar["Cantidad"],
        color=["b","g","c","m","y"])
plt.show()

# Grafica de pastel
plt.plot(df_juegos["Nombre"], df_juegos["Cantidad"])
plt.pie(df_juegos["Cantidad"], labels=df_juegos["Nombre"])
plt.show()

print("Angela Correa NC = 0037")
