# Función para imprimir la tabla de verdad de la compuerta OR
def tabla_verdad_or():
    print("A\tB\tA OR B")
    print("--------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = a or b
            print(f"{a}\t{b}\t{resultado}")

# Llamar a la función
tabla_verdad_or()
