class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("✅ Producto agregado al carrito")

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def ver_carrito(self):
        return self.productos

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.obtener_precio()
        return total

    def vaciar(self):
        self.productos.clear()
        
