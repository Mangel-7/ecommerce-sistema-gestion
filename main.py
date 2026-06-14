from usuarios import registrar_usuario
from productos import agregar_producto, listar_productos
from carrito import Carrito
from ventas import registrar_venta

carrito = Carrito()
usuario_actual = None

while True:
    print("\n--- MENU ---")
    print("1. Registrar usuario")
    print("2. Agregar producto")
    print("3. Ver productos")
    print("4. Agregar producto al carrito")
    print("5. Ver carrito")
    print("6. Comprar")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    # Registrar usuario
    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        usuario_actual = registrar_usuario(nombre, correo)
        print("Usuario registrado correctamente")

    # Agregar producto
    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio: "))
            agregar_producto(nombre, precio)
        except:
            print("Error: Ingrese un número válido")

    # Ver productos
    elif opcion == "3":
        productos = listar_productos()
        if productos:
            for i, p in enumerate(productos):
                print(f"{i}. {p.obtener_nombre()} - ${p.obtener_precio()}")
        else:
            print("No hay productos")

    # Agregar al carrito
    elif opcion == "4":
        productos = listar_productos()
        if productos:
            for i, p in enumerate(productos):
                print(f"{i}. {p.obtener_nombre()}")

            try:
                opcion_prod = int(input("Seleccione producto: "))
                if 0 <= opcion_prod < len(productos):
                    carrito.agregar_producto(productos[opcion_prod])
                else:
                    print("Opción inválida")
            except:
                print("Error: debe ingresar un número")
        else:
            print("No hay productos disponibles")

    # Ver carrito
    elif opcion == "5":
        if carrito.ver_carrito():
            for p in carrito.ver_carrito():
                print(f"{p.obtener_nombre()} - ${p.obtener_precio()}")

            print("Total:", carrito.calcular_total())
        else:
            print("Carrito vacío")

    # Comprar
    elif opcion == "6":
        if usuario_actual:
            if carrito.ver_carrito():
                venta = registrar_venta(usuario_actual, carrito)
                print("Compra realizada con éxito")
                print("Total:", venta.total)

                carrito.vaciar()
            else:
                print("Carrito vacío")
        else:
            print("Debe registrar un usuario primero")

    # Salir
    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
        
