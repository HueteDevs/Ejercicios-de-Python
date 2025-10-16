'''
================================================================================
Escribir un programa que declare la variable "d" y le asigne el valor 5, y 
verifique si esta variable es mayor o menor que 0. Si la variable es mayor que 
0, el programa debe imprimir "positiva", de lo contrario debe imprimir 
"Negativa".
================================================================================

**** CÓMO SE HACE ***
- Declaramos la variable d
- Usamos el condicional [if: else:] para que compruebe que la variable mayor o
  menor que 0, en este caso va a comprobar que sea mayor (>)
- Si no es mayor que 0 nos devolverá que es Negativo y si lo es,
  nos devolverá que es positivo mediante un print().

''' 
d = 5

if d > 0:
  print("Positivo")
else:
  print("Negativo")