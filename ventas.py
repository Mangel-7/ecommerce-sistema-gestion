def generar_venta(carrito):
    return {
        "productos": carrito,
        "total": sum(p["precio"] for p in carrito)
    }
