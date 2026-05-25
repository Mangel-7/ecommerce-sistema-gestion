from productos import agregar_producto, listar_productos

productos = []

producto1 = {"id": 1, "nombre": "Laptop", "precio": 800}
producto2 = {"id": 2, "nombre": "Mouse", "precio": 20}

productos = agregar_producto(productos, producto1)
productos = agregar_producto(productos, producto2)

listar_productos(productos)
