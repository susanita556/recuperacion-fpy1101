def calcular_descuento(subtotal):
    
    if subtotal >= 50000:
        return subtotal * 0.10
    else:
        return 0

def mostrar_resultado(nombre_producto, subtotal, descuento, total):
  
    print("\n" + "="*30)
    print("      RESULTADO DE LA VENTA")
    print("="*30)
    print(f"Producto:   {nombre_producto}")
    print(f"Subtotal:   ${subtotal}")
    print(f"Descuento:  ${descuento}")
    print(f"Total:      ${total}")
    print("="*30 + "\n")


# --- PROGRAMA PRINCIPAL ---
continuar = "s"

while continuar.lower() == "s":
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").strip()
        if nombre_producto != "":
            break
        print("Error: El nombre no puede estar vacío.")

     while True:
        try:
            precio_unitario = int(input("Ingrese el precio unitario: "))
            if precio_unitario > 0:
                break
            else:
                print("Error: El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: El precio debe ser un número entero.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad comprada: "))
            if cantidad > 0:
                break
            else:
                print("Error: La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    # Proceso de cálculos utilizando variables descriptivas
    subtotal = precio_unitario * cantidad
    descuento = calcular_descuento(subtotal)
    total = subtotal - descuento

    # Salida: Llamar a la función para mostrar resultados
    mostrar_resultado(nombre_producto, subtotal, descuento, total)

    # Preguntar si desea realizar otra venta
    while True:
        continuar = input("¿Desea realizar otra venta? (s/n): ").strip().lower()
        if continuar in ["s", "n"]:
            break
        print("Error: Ingrese una opción válida ('s' para Sí, 'n' para No).")

print("\nPrograma finalizado.")
