# El diccionario que define una relacion uno a uno entre claves y valores 

Datos_basicos = {"Nombres": "Juan Carlos",
                 "Apellidos": "Perez Garcia",
                 "DUI": "01025487-9",
                 "Fecha_Nacimiento": "23/07/1980",
                 "Lugar_Nacimiento": "Soya City",
                 "Nacionalidad": "Salvadoreña",
                 "Estado_civil": "Esperando_Milagro",
                 }

print("\nDetalle del Diccionario")
print("=============================")

print("\nClaves de diccionario: ", Datos_basicos.keys())
print("\nClaves de diccionario: ", Datos_basicos.values())
print("\nClaves de diccionario: ", Datos_basicos.items())

#Ejemplos practicos de los diccionarios 
print("\nIncripcion del curso")
print("=========================")

print("\nDatos del participante")
print("===========================")

print("DUI: ", Datos_basicos["DUI"])
print("Nombre Completo: ", Datos_basicos["Nombres"]+" "+Datos_basicos["Apellidos"])