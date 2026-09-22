# Examen práctico - Terminal de Expedición Espacial
# Nombre y apellido:Benjamin Moyano
# Curso: 2 1
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de destinos y costos.
# Pedir el nombre del piloto.

# =========================
# ETAPA 2 - NAVEGACIÓN
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener destino y costo.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.

a = input("escriba su nombre: ")
combustible = int(100)
viajes = int(0)
viajeluna = int(0)
viajemarte = int(0)
viajesaturno = int(0)

destinos = ["Luna", "Marte", "Saturno"]
Costos = [20, 35, 50]
print("TERMINAL DE EXPLORACIÓN ESPACIAL")
print("bienvenido sea", a)
print("su combustible total es de", combustible)

#no se como hacer la menu profe jeje, asi que el practico me carreara la nota, creo

print("se ira a la", destinos[0])
print("su costo es de", Costos[0])

print("viaje realizado, ahora su combustible es de")
print(combustible - Costos[0])
