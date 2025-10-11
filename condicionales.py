'''
================================================================================
Crear una serie de instrucciones en Python que permitan declarar una variable 
"var" y asignarle el valor "Hola". Luego, el programa debe verificar si la 
variable var es un entero o una cadena de caracteres. Si es un entero, el 
programa debe imprimir en la consola "Entero", y si es una cadena de caracteres, 
el programa imprimirá "Cadena de caracteres" en la consola".
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