"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7


Enunciat:

Implementa una funció anomenada find_max(lst) que trobi el valor màxim en una
llista de números utilitzant recursió. La funció ha de tornar el valor
màxim de la llista.

Paràmetres:
     lst (List): llista de nombres enters o flotants

Exemple:
     Entrada:
     numbers_list = [1, 5, 2, 7, 3]
     fid_max(numbers_list)

     Sortida:
     7

"""


def find_max(lst):
    # Write here your code
    
    # Validamos la entrada
    if not isinstance(lst, list):
        raise ValueError("ERROR. Se esperaba una lista.")

    # Introducimos la condición de salida que será el ultimo elemento de la lista.
    if len(lst) == 1:
        return lst[0]

    # Miramos si el elemento actual es mayor que el que miremos del resto de la lista.
    MaxAct = find_max(lst[1:])
    if lst[0] > MaxAct :
        return lst[0]

    # Si el actual no es mas grande devolvemos el que teníamos.
    return MaxAct
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
numbers_list = [1, 5, 2, 7, 3]
print(find_max(numbers_list))
