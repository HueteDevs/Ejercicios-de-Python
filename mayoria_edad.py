'''
================================================================================
Escribir un programa que solicite al usuario su edad y la almecene en una 
variable. El programa debe verificar si el usuario tiene una edad mayor o 
menor a 18 años. Si la edad del usuario es mayor o igual a 18, entonces 
el programa debe imprimir "El usuario es mayor de edad", de lo contrario 
debe imprimir "El usuario es menor de edad".
================================================================================

**** CÓMO SE HACE ***
- Declaramos la variable edad y le damos el valor que introduzca el usuario
  mediante un input() *TIP* [Para que no tengamos ningún problema, podemos
  convertir directamente el valor que introduzca el usuario en un entero mediante
  la función int(print())]
- Usamos el condicional (if-else) para comprobar que la edad del usuario es mayor
  de edad
- Si el usuario es mayor o menor de edad imprimimos el mensaje 
  que corresponda mediante el print().
  
'''
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")
