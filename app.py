from flask import Flask, request, jsonify
from usuarios import registrar_usuario, listar_usuarios
from productos import agregar_producto, listar_productos
from carrito import Carrito
from ventas import registrar_venta

app = Flask(__name__)

# Simulación global
carrito = Carrito()
usuario_actual = None

# =========================
# 1. REGISTRAR USUARIO
# =========================
@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    global usuario_actual

    data = request.json
    usuario_actual = registrar_usuario(data["nombre"], data["correo"])

    return jsonify({
        "mensaje": "Usuario registrado",
        "nombre": usuario_actual.obtener_nombre()
    }), 201


# =========================
# 2. LISTAR USUARIOS
# =========================
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    lista = []

    for u in listar_usuarios():
        lista.append({
            "nombre": u.obtener_nombre(),
            "correo": u.obtener_correo()
        })

    return jsonify(lista)


# =========================
# 3. AGREGAR PRODUCTO
# =========================
@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.json

    agregar_producto(data["nombre"], float(data["precio"]))

    return jsonify({"mensaje": "Producto agregado"}), 201


# =========================
# 4. LISTAR PRODUCTOS
# =========================
@app.route("/productos", methods=["GET"])
def obtener_productos():
    lista = []

    for p in listar_productos():
        lista.append({
            "nombre": p.obtener_nombre(),
            "precio": p.obtener_precio()
        })

    return jsonify(lista)


# =========================
# 5. AGREGAR AL CARRITO
# =========================
@app.route("/carrito", methods=["POST"])
def agregar_carrito():
    data = request.json
    index = data["indice"]

    productos = listar_productos()

    if 0 <= index < len(productos):
        carrito.agregar_producto(productos[index])
        return jsonify({"mensaje": "Producto agregado al carrito"})
    else:
        return jsonify({"error": "Índice inválido"}), 400


# =========================
# 6. VER CARRITO
# =========================
@app.route("/carrito", methods=["GET"])
def ver_carrito():
    lista = []

    for p in carrito.ver_carrito():
        lista.append({
            "nombre": p.obtener_nombre(),
            "precio": p.obtener_precio()
        })

    return jsonify({
        "productos": lista,
        "total": carrito.calcular_total()
    })


# =========================
# 7. ELIMINAR PRODUCTO DEL CARRITO
# =========================
@app.route("/carrito", methods=["DELETE"])
def eliminar_carrito():
    data = request.json
    indice = data["indice"]

    try:
        carrito.eliminar_producto(indice)
        return jsonify({"mensaje": "Producto eliminado"})
    except:
        return jsonify({"error": "Error al eliminar"}), 400


# =========================
# 8. REALIZAR COMPRA
# =========================
@app.route("/ventas", methods=["POST"])
def comprar():
    global usuario_actual

    if usuario_actual is None:
        return jsonify({"error": "No hay usuario registrado"}), 400

    if not carrito.ver_carrito():
        return jsonify({"error": "Carrito vacío"}), 400

    venta = registrar_venta(usuario_actual, carrito)
    total = venta.total

    carrito.vaciar()

    return jsonify({
        "mensaje": "Compra realizada",
        "total": total
    })


# =========================
# 9. LISTAR VENTAS (EXTRA)
# =========================
@app.route("/ventas", methods=["GET"])
def listar_ventas():
    return jsonify({"mensaje": "Ventas registradas correctamente"})


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    app.run(debug=True)
