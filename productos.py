import uuid

class Producto:
    def __init__(self, nombre, precio):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._precio = precio

    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio


productos = []

def agregar_producto(nombre, precio):
    try:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        producto = Producto(nombre, precio)
        productos.append(producto)
        print("✅ Producto agregado correctamente")

    except ValueError as e:
        print("Error:", e)

def listar_productos():
    return productos
