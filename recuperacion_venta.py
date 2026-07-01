def calcular_descuento(subtotal):
  
    if subtotal >= 50000:
        return subtotal * 0.10
    else:
        return 0.0

def mostrar_resultado(nombre_producto, subtotal, descuento, total):
    
    print("\n" + "="*30)
    print("      RESULTADO DE LA VENTA")
    print("="*30)
    print(f"Producto:   {nombre_producto}")
    print(f"Subtotal:   ${subtotal:,.0f}")
    print(f"Descuento:  ${descuento:,.0f}")
    print(f"Total:      ${total:,.0f}")
    print("="*30 + "\n")


continuar = "s"

while continuar.lower() == "s":
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").strip()
        if nombre_producto != "":
            break
        print("Error: El nombre del producto no puede estar vacío.")
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario: "))
            if precio_unitario > 0:
                break
            else:
                print("Error: El precio debe ser mayor que cero.")
        except ValueError:
            print("Error: El precio debe ser un valor numérico.")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad comprada: "))
            if cantidad > 0:
                break
            else:
                print("Error: La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    subtotal_venta = precio_unitario * cantidad

    descuento_venta = calcular_descuento(subtotal_venta)

    total_venta = subtotal_venta - descuento_venta

    mostrar_resultado(nombre_producto, subtotal_venta, descuento_venta, total_venta)

    while True:
        continuar = input("¿Desea realizar otra venta? (s/n): ").strip().lower()
        if continuar in ["s", "n"]:
            break
        print("Error: Ingrese una opción válida ('s' para Sí, 'n' para No).")

print("\nPrograma finalizado.")
