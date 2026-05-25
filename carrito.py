def agregar_al_carrito(carrito, producto):
    return carrito + [producto]

def calcular_total(carrito):
    return sum(p["precio"] for p in carrito)
