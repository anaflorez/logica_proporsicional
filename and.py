def tabla_verdad_and():
    print("A\tB\tA AND B")
    print("--------------------")
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = a and b
            print(f"{a}\t{b}\t{resultado}")

# Llamar a la función
tabla_verdad_and()
