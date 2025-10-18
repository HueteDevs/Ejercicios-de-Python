'''
================================================================================
Escribir un programa que declare la variable "d" y le asigne el valor 5, y 
verifique si esta variable es mayor o menor que 0. Si la variable es mayor que 
0, el programa debe imprimir "positiva", de lo contrario debe imprimir 
"Negativa".
================================================================================

**** CÓMO SE HACE ***
- Declaramos la variable var
- Usamos el condicional [if: else:] para que compruebe que la variable es un 
  entero con type()
- Si no es un entero nos tiene que devolver un mensaje diciendo que es una
  cadena mediante un print()

''' 
var = "Hola"

if type(var) == int:
    print("Entero")
else:
    print("Es una cadena")