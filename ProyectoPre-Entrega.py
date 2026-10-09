# Pre-entrega del proyecto - Python Inicial
# Sistema de gestión básica de productos
# Cada producto se guarda como una sublista: [nombre, categoria, precio]
# Todos los productos se guardan en la lista "productos".

productos = []

while True:
    print("\n" + "-" * 40)
    print("  SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS")
    print("-" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Ingresá una opción: ").strip()

    # ---------- 1. AGREGAR ----------
    if opcion == "1":
        print("\n>> Agregar producto")

        nombre = input("Nombre: ").strip()
        while nombre == "":
            print("El nombre no puede quedar vacío.")
            nombre = input("Nombre: ").strip()

        categoria = input("Categoría: ").strip()
        while categoria == "":
            print("La categoría no puede quedar vacía.")
            categoria = input("Categoría: ").strip()

        precio = input("Precio (número entero, sin centavos): ").strip()
        while not precio.isdigit() or int(precio) == 0:
            print("El precio tiene que ser un número entero mayor a 0.")
            precio = input("Precio (número entero, sin centavos): ").strip()
        precio = int(precio)

        producto = [nombre, categoria, precio]
        productos.append(producto)
        print(f"Producto '{nombre}' agregado correctamente.")

    # ---------- 2. MOSTRAR ----------
    elif opcion == "2":
        print("\n>> Lista de productos")
        if len(productos) == 0:
            print("No hay productos cargados.")
        else:
            numero = 1
            for producto in productos:
                print(f"{numero}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                numero += 1
            print(f"Total de productos: {len(productos)}")

    # ---------- 3. BUSCAR ----------
    elif opcion == "3":
        print("\n>> Buscar producto")
        if len(productos) == 0:
            print("No hay productos cargados.")
        else:
            buscado = input("Ingresá el nombre a buscar: ").strip().lower()
            while buscado == "":
                print("Tenés que escribir algo para buscar.")
                buscado = input("Ingresá el nombre a buscar: ").strip().lower()

            encontrados = 0
            numero = 1
            for producto in productos:
                if buscado in producto[0].lower():
                    print(f"{numero}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                    encontrados += 1
                numero += 1

            if encontrados == 0:
                print("No se encontraron resultados.")

    # ---------- 4. ELIMINAR ----------
    elif opcion == "4":
        print("\n>> Eliminar producto")
        if len(productos) == 0:
            print("No hay productos cargados.")
        else:
            numero = 1
            for producto in productos:
                print(f"{numero}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                numero += 1

            posicion = input("Número del producto a eliminar: ").strip()
            while not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(productos):
                print(f"Ingresá un número entre 1 y {len(productos)}.")
                posicion = input("Número del producto a eliminar: ").strip()

            eliminado = productos.pop(int(posicion) - 1)
            print(f"Producto '{eliminado[0]}' eliminado.")

    # ---------- 5. SALIR ----------
    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Elegí un número del 1 al 5.")