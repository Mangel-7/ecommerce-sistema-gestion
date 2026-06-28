import threading
import time

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

def procesar_venta(venta):
    print("⏳ Procesando venta...")
    time.sleep(2)
    print(f"Venta procesada correctamente. Total: {venta.total}")


def registrar_venta(usuario, carrito):
    venta = Venta(usuario, carrito.productos.copy())
    ventas.append(venta)

    # Concurrencia (no bloquea el sistema)
    hilo = threading.Thread(target=procesar_venta, args=(venta,))
    hilo.start()

    return venta
