
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




#Ejercicio 3.	Cree una función lambda con la misma funcionalidad 
# que la función de suma que acaba de crear.

resultado = lambda a,b,c: a+b+c



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

for i in lista_nombre:
    if nombre == i:
        print("El nombre coincide con el valor de la lista")
        break
    else:
        print("El nombre no coincide con ningún valor de la lista")
        break
            
        