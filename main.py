from usuarios import registrar_usuario
from productos import agregar_producto, listar_productos
from carrito import Carrito
from ventas import registrar_venta

carrito = Carrito()
usuario_actual = None

while True:
    print("\n--- MENU ---")
    print("1. Registrar usuario")
    print("2. Agregar productos")
    print("3. Ver productos")
    print("4. Agregar productos al carrito")
    print("5. Ver carrito")
    print("6. Comprar")
    print("7. Salir")
    print("8. Eliminar producto del carrito")

    opcion = input("Seleccione una opción: ")

    # 1 Registrar usuario
    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        usuario_actual = registrar_usuario(nombre, correo)
        print("Usuario registrado correctamente")

    # 2 Agregar múltiples productos
    elif opcion == "2":
        while True:
            nombre = input("Nombre del producto (o 'salir'): ")

            if nombre.lower() == "salir":
                break

            try:
                precio = float(input("Precio: "))
                agregar_producto(nombre, precio)
            except:
                print("Error: Ingrese un número válido")

    # 3 Ver productos
    elif opcion == "3":
        productos = listar_productos()
        if productos:
            print("\n--- PRODUCTOS ---")
            for i, p in enumerate(productos):
                print(f"{i}. {p.obtener_nombre()} - ${p.obtener_precio()}")
        else:
            print("No hay productos")

    # 4 Agregar múltiples al carrito
    elif opcion == "4":
        productos = listar_productos()

        if productos:
            while True:
                print("\n--- PRODUCTOS ---")
                for i, p in enumerate(productos):
                    print(f"{i}. {p.obtener_nombre()} - ${p.obtener_precio()}")

                opcion_prod = input("Seleccione producto (o 'salir'): ")

                if opcion_prod.lower() == "salir":
                    break

                try:
                    opcion_prod = int(opcion_prod)
                    if 0 <= opcion_prod < len(productos):
                        carrito.agregar_producto(productos[opcion_prod])
                    else:
                        print("Opción inválida")
                except:
                    print("Error: debe ingresar un número")
        else:
            print("No hay productos disponibles")

    # 5 Ver carrito
    elif opcion == "5":
        carrito.mostrar_carrito()

    # 6 Comprar
    elif opcion == "6":
        if usuario_actual:
            if carrito.ver_carrito():
                confirm = input("¿Confirmar compra? (si/no): ")

                if confirm.lower() == "si":
                    venta = registrar_venta(usuario_actual, carrito)
                    print("Compra realizada")
                    carrito.vaciar()
                else:
                    print("Compra cancelada")
            else:
                print("Carrito vacío")
        else:
            print("Debe registrar un usuario primero")

    # 7 Salir
    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    # 8 Eliminar producto
    elif opcion == "8":
        if carrito.ver_carrito():
            carrito.mostrar_carrito()

            try:
                eliminar = int(input("Seleccione índice a eliminar: "))
                carrito.eliminar_producto(eliminar)
            except:
                print("Error: ingrese un número válido")
        else:
            print("Carrito vacío")

    else:
        print("Opción inválida")
