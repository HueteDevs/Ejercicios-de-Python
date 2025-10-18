print("=" * 90)
print('''
    *** TUPLA INMUTABLE ***
Crea una tupla pokemon_base con: (nombre, tipo_principal, nivel_inicial)
 
 * Comprueba acceso por índice y desempaquetado.
 * Intenta “cambiar” el nivel dentro de la tupla (debería fallar) y explica 
   por qué en un print explicativo.
   ''')
print("=" * 90)
print()
POKEMON_BASE = ("Sprigatito","planta",1)
print(POKEMON_BASE[0])

nombre,tipo_principal,nivel_inicial = POKEMON_BASE
print(nombre,tipo_principal,nivel_inicial)


#====INTENTO DE CAMBIO DE TUPLA===
# POKEMON_BASE[2] = 2

print('''TypeError: 'tuple' object does not support item assignment, este error 
      sale porque las tuplas no se pueden modificar, son inmutables.''')
print()

print("=" * 90)
print('''
    *** TUPLA COMO CLAVE***
Crea diccionario registro_capturas donde la clave sea la tupla (ruta,hora), y
el valor sea el nombre del pokemon.
 
 * Añade 3 capturas.
 * Pregunta si existe una clave concreta usando in.
   ''')
print("=" * 90)
print()
CAPTURA = (1, 1.50)
CAPTURA_2 = (1, 1.75)
CAPTURA_3 = (2, 2) 
ruta,hora = CAPTURA 
registro_capturas= {
    CAPTURA : "Sprigatito",
    CAPTURA_2 : "Pawmi",
    CAPTURA_3 : "Pichu",
}


print(registro_capturas)

print((1,1.50) in registro_capturas)
print()
print("=" * 90)
print('''
    ***RANKING COMPACTO***
Crea una lista de tuplas ranking = [(nombre,nivel),...]
 
 * Recorre la lista y muestra "#1 NOMBRE-NIVEL X", etc.
 * Encuentra la tupla con mayor nivel sin usar funciones avanzadas (solo bucles
   y condicionales).
   ''')

ranking = []

POKEMON = ("Sprigatito",10)
POKEMON_2 = ("Pawmi",8)
POKEMON_3 = ("Pichu",7)

ranking.append(POKEMON)
ranking.append(POKEMON_2)
ranking.append(POKEMON_3)
print(ranking)

posicion = 1
for nombre,nivel in ranking:
    print(f"#{posicion} {nombre} | {nivel}")
    posicion += 1
    
nivel_mayor = 0
pokemon_mayor = ""

for nombre, nivel in ranking:
     # ¿Es este nivel mejor que el mejor que llevaba?
    if nivel > nivel_mayor : # OJO: comparación en este sentido
        nivel_mayor = nivel  # actualizas el mejor nivel
        pokemon_mayor = nombre # y guardas el nombre asociado

print(f"El nivel más alto es del pokemon {pokemon_mayor}, con nivel: {nivel_mayor}")