class Venta:
    def __init__(self, usuario, productos):
        self.usuario = usuario
        self.productos = productos
        self.total = self.calcular_total()

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.obtener_precio()
        return total


ventas = []

def registrar_venta(usuario, carrito):
    venta = Venta(usuario, carrito.productos)
    ventas.append(venta)
    return venta
