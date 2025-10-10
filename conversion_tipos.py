'''
================================================================================
Escriba una serie de instrucciones de Python que permita declarar 2 variables 
'x' e 'y' asignándoles respectivamente los valores 3 y 8.5, luego convertir el 
tipo de estas variables a una cadena de caracteres. AL final, el programa debe 
mostrar el tipo de estas variables después de la conversión.
================================================================================

*** CÓMO SE HACE ***
- Asignamos los valores a las variables 'x' e 'y'.
- Después cambiamos el tipo de las variables usando str()
- Por último mostramos los tipos de las variables con un print() y un type() 

'''
x = 3
y = 8.5

x = str(x)
y = str(y)

print(type(x))
print(type(y))