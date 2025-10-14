'''
================================================================================
Escribir la instrucción que permite crear una lista de números del 1 al 10
utilizando la comprensión de listas.
================================================================================

*** CÓMO SE HACE ***
- Con la comprensión de listas podemos crear una lista directamente, sin usar 
  append().
- Dentro de los corchetes ponemos una expresión seguida de un bucle for.
- range(1, 10 + 1) genera los números del 1 al 10.
- Por último, mostramos la lista resultante con print().

'''

cuenta= [n for n in range(1, 10 +1)]
print(cuenta)
 