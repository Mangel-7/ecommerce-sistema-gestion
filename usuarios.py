import uuid

class Usuario:
    def __init__(self, nombre, correo):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._correo = correo

    def obtener_nombre(self):
        return self._nombre

    def obtener_correo(self):
        return self._correo


usuarios = []

def registrar_usuario(nombre, correo):
    usuario = Usuario(nombre, correo)
    usuarios.append(usuario)
    return usuario

def listar_usuarios():
    return usuarios
