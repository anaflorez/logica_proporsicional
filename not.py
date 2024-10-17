# Función para imprimir la tabla de verdad de la compuerta NOT
def tabla_verdad_not():
    print("A\tNOT A")
    print("----------------")
    for a in [0, 1]:
        resultado = not a
        print(f"{a}\t{int(resultado)}")

# Llamar a la función
tabla_verdad_not()
