
#Ejercicio 1.	Cree un bucle For de Python.

productos = {'uno':"verdura", 'dos':"legumbre", 'tres':"pescado"}
for producto in productos.values():
    print(producto)

"""Imprime:
verdura
legumbre
pescado
"""


#Ejercicio 2.	Cree una función de Python llamada suma que tome 3 
# argumentos y devuelva la suma de los 3.

def suma(a, b, c):
    resultado = a + b + c
    return resultado


print(suma(1,2,3))




#Ejercicio 3.	Cree una función lambda con la misma funcionalidad 
# que la función de suma que acaba de crear.

resultado = lambda a,b,c: a+b+c
print(resultado(1,2,3))



#Ejercicio 4. 

"""
-Utilizando la siguiente lista y variable, 
determine si el valor de la variable
coincide o no con un valor de la lista. 
*Sugerencia, si es necesario, utilice un bucle 
for in y el operador in.

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'"""


nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print("El nombre coincide con el valor de la lista")

else:
    print('¡NO COINCIDE CON NINGÚN VALOR!')
            
        