#escribe esta linea de codigo:
print("Bienvenidos al entrenamiento con python, vamos disfrutar al maximo esta sesión")

"""
    Descuento en una compra:
    Si compras mas de $1000, obtienes un descuesto del 20%
    Pide el monto de la compra y muestra el precion final
"""

# Pedir datos por teclado al usuario int entero float decimales str cadenas de caracteres bool booleanos

compra = float(input("digite el valor de la compra: "))

# Si compras mas de $1000, obtienes un descuesto del 20%
# Siempre que la salida tenga mas de un camino de resolucion, debo implementar condicionales

# operadores combinados
# operadores de asignacion =, operadores aritmeticos +-*/ , operadores logicos and y, or o, not,
# #operadores de comparacion ==, !=,  >, <, >=, <=

if compra > 1000:
    descuento = compra * 0.2
    #compra = compra - descuento # operador de asignacion 
    compra -= descuento # operador de asignacion compuesto
    print (f"el descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")