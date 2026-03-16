import math

# ==============================================
# PROGRAMA: Calculadora de Figuras Geométricas
# DESCRIPCIÓN: Menú con 10 opciones para calcular
# variables geométricas de figuras 2D y 3D.
# ==============================================

opcion = 0

while opcion != 10:

    # ==========================================
    # MENÚ PRINCIPAL
    # ==========================================
    print("========================================")
    print("      CALCULADORA GEOMÉTRICA")
    print("========================================")
    print("-- FIGURAS 2D --------------------------")
    print("1. Circulo")
    print("2. Rectangulo")
    print("3. Triangulo equilatero")
    print("4. Trapecio")
    print("-- FIGURAS 3D --------------------------")
    print("5. Esfera")
    print("6. Cilindro")
    print("7. Paralelepipedo")
    print("8. Cono")
    print("-- ESPECIAL ----------------------------")
    print("9. Triangulo rectangulo 2D")
    print("10. Salir")
    print("========================================")

    opcion = int(input("Seleccione una opcion (1-10): "))

    # ==========================================
    # OPCION 1 — CIRCULO
    # ==========================================
    if opcion == 1:
        print("\n--- CIRCULO ---")
        radio = float(input("Ingrese el radio (float): "))

        area      = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio

        print("Area:     ", round(area, 4), "u2")
        print("Perimetro:", round(perimetro, 4), "u")

    # ==========================================
    # OPCION 2 — RECTANGULO
    # ==========================================
    elif opcion == 2:
        print("\n--- RECTANGULO ---")
        base   = float(input("Ingrese la base (float): "))
        altura = float(input("Ingrese la altura (float): "))

        area      = base * altura
        perimetro = 2 * (base + altura)

        print("Area:     ", round(area, 4), "u2")
        print("Perimetro:", round(perimetro, 4), "u")

    # ==========================================
    # OPCION 3 — TRIANGULO EQUILATERO
    # ==========================================
    elif opcion == 3:
        print("\n--- TRIANGULO EQUILATERO ---")
        lado = float(input("Ingrese el lado (float): "))

        area      = (math.sqrt(3) / 4) * lado ** 2
        perimetro = 3 * lado

        print("Area:     ", round(area, 4), "u2")
        print("Perimetro:", round(perimetro, 4), "u")

    # ==========================================
    # OPCION 4 — TRAPECIO
    # ==========================================
    elif opcion == 4:
        print("\n--- TRAPECIO ---")
        base_mayor = float(input("Ingrese la base mayor (float): "))
        base_menor = float(input("Ingrese la base menor (float): "))
        altura     = float(input("Ingrese la altura (float): "))
        lado_a     = float(input("Ingrese el lado lateral A (float): "))
        lado_b     = float(input("Ingrese el lado lateral B (float): "))

        area      = ((base_mayor + base_menor) / 2) * altura
        perimetro = base_mayor + base_menor + lado_a + lado_b

        print("Area:     ", round(area, 4), "u2")
        print("Perimetro:", round(perimetro, 4), "u")

    # ==========================================
    # OPCION 5 — ESFERA
    # ==========================================
    elif opcion == 5:
        print("\n--- ESFERA ---")
        radio = float(input("Ingrese el radio (float): "))

        volumen          = (4 / 3) * math.pi * radio ** 3
        area_superficial = 4 * math.pi * radio ** 2

        print("Volumen:         ", round(volumen, 4), "u3")
        print("Area superficial:", round(area_superficial, 4), "u2")

    # ==========================================
    # OPCION 6 — CILINDRO
    # ==========================================
    elif opcion == 6:
        print("\n--- CILINDRO ---")
        radio  = float(input("Ingrese el radio de la base (float): "))
        altura = float(input("Ingrese la altura (float): "))

        volumen          = math.pi * radio ** 2 * altura
        area_superficial = 2 * math.pi * radio * (radio + altura)

        print("Volumen:         ", round(volumen, 4), "u3")
        print("Area superficial:", round(area_superficial, 4), "u2")

    # ==========================================
    # OPCION 7 — PARALELEPIPEDO
    # ==========================================
    elif opcion == 7:
        print("\n--- PARALELEPIPEDO ---")
        largo = float(input("Ingrese el largo (float): "))
        ancho = float(input("Ingrese el ancho (float): "))
        alto  = float(input("Ingrese el alto (float): "))

        volumen          = largo * ancho * alto
        area_superficial = 2 * (largo * ancho + largo * alto + ancho * alto)

        print("Volumen:         ", round(volumen, 4), "u3")
        print("Area superficial:", round(area_superficial, 4), "u2")

    # ==========================================
    # OPCION 8 — CONO
    # ==========================================
    elif opcion == 8:
        print("\n--- CONO ---")
        radio  = float(input("Ingrese el radio de la base (float): "))
        altura = float(input("Ingrese la altura (float): "))

        generatriz       = math.sqrt(radio ** 2 + altura ** 2)
        volumen          = (1 / 3) * math.pi * radio ** 2 * altura
        area_superficial = math.pi * radio * (radio + generatriz)

        print("Generatriz:      ", round(generatriz, 4), "u")
        print("Volumen:         ", round(volumen, 4), "u3")
        print("Area superficial:", round(area_superficial, 4), "u2")

    # ==========================================
    # OPCION 9 — TRIANGULO RECTANGULO
    # ==========================================
    elif opcion == 9:
        print("\n--- TRIANGULO RECTANGULO ---")
        cateto_a = float(input("Ingrese el cateto A (float): "))
        cateto_b = float(input("Ingrese el cateto B (float): "))

        hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
        area       = (cateto_a * cateto_b) / 2
        perimetro  = cateto_a + cateto_b + hipotenusa

        print("Hipotenusa:", round(hipotenusa, 4), "u")
        print("Area:      ", round(area, 4), "u2")
        print("Perimetro: ", round(perimetro, 4), "u")

    # ==========================================
    # OPCION 10 — SALIR
    # ==========================================
    elif opcion == 10:
        print("\nHasta luego! Cerrando programa...")

    # ==========================================
    # OPCION INVALIDA
    # ==========================================
    else:
        print("\nOpcion invalida. Ingrese un numero entre 1 y 10.")

# ==============================================
# RESUMEN GENERAL DEL PROGRAMA
# Este programa muestra un menu con 10 opciones.
# Opciones 1-4: figuras 2D (area y perimetro).
# Opciones 5-8: figuras 3D (volumen y area superficial).
# Opcion 9: triangulo rectangulo 2D.
# Opcion 10: sale del programa.
# El while mantiene el menu activo hasta elegir 10.
# ==============================================