class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado al carrito")

    def eliminar_producto(self, indice):
        try:
            if 0 <= indice < len(self.productos):
                eliminado = self.productos.pop(indice)
                print(f"Producto eliminado: {eliminado.obtener_nombre()}")
            else:
                print("Índice inválido")
        except:
            print("Error al eliminar producto")

    def ver_carrito(self):
        return self.productos

    def mostrar_carrito(self):
        if not self.productos:
            print("Carrito vacío")
            return

        print("\n--- CARRITO ---")
        for i, p in enumerate(self.productos):
            print(f"{i}. {p.obtener_nombre()} - ${p.obtener_precio()}")

        print(f"TOTAL: ${self.calcular_total()}")

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.obtener_precio()
        return total

    def vaciar(self):
        self.productos.clear()
