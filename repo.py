# =========================================
# INVENTORY SYSTEM
# =========================================
# Este programa permite:
# - Agregar productos
# - Mostrar inventario
# - Calcular estadísticas
# - Validar entradas del usuario

# Lista principal donde se guardan los productos
inventario = []

# =========================================
# FUNCTION: VALIDAR NÚMERO
# =========================================
def validar_numero(mensaje, tipo):
    while True:
        valor = input(mensaje)
        try:
            if tipo == "int":
                valor = int(valor)
            elif tipo == "float":
                valor = float(valor)

            if valor < 0:
                print("Error: no se permiten valores negativos.")
            else:
                return valor
        except:
            print("Error: ingrese un número válido.")

# =========================================
# FUNCTION: AGREGAR PRODUCTO
# =========================================
def agregar_producto(inventario):
    print("\n--- Agregar Producto ---")

    nombre = input("Nombre del producto: ").strip()
    while nombre == "":
        print("Error: el nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()

    precio = validar_numero("Precio: ", "float")
    cantidad = validar_numero("Cantidad: ", "int")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")

# =========================================
# FUNCTION: MOSTRAR INVENTARIO
# =========================================
def mostrar_inventario(inventario):
    print("\n--- Inventario ---")

    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    for producto in inventario:
        print(
            f"Producto: {producto['nombre']} | "
            f"Precio: {producto['precio']} | "
            f"Cantidad: {producto['cantidad']}"
        )

# =========================================
# FUNCTION: CALCULAR ESTADÍSTICAS
# =========================================
def calcular_estadisticas(inventario):
    print("\n--- Estadísticas ---")

    if len(inventario) == 0:
        print("No hay datos para calcular.")
        return

    total_valor = 0
    total_productos = 0

    for producto in inventario:
        total_valor += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"Valor total del inventario: {total_valor}")
    print(f"Cantidad total de productos: {total_productos}")

# =========================================
# MAIN (MENÚ PRINCIPAL)
# =========================================
def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(inventario)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            calcular_estadisticas(inventario)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Error: opción inválida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()


