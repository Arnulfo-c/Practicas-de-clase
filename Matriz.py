filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))

matriz =[]
print("\nPor favor, ingrese los valores de la matriz:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Elemento[{i+1}][{j+1}]: "))
        fila.append(valor)
        matriz.append(fila)

print("\nLa matriz ingresada es: ")
for fila in matriz:
    print(fila)