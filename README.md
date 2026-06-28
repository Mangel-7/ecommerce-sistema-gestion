# 🛒 Sistema de Gestión de E-commerce

## 📌 Descripción
Este proyecto consiste en el desarrollo de un sistema de gestión de e-commerce que permite administrar usuarios, productos, carrito de compras y ventas.

El sistema fue desarrollado en Python e implementado como una API REST utilizando Flask, permitiendo la interacción mediante servicios web.

---

## 🎯 Objetivo
Simular el funcionamiento de una tienda virtual aplicando conceptos de programación estructurada, POO, concurrencia y servicios web.

---

## ⚙️ Tecnologías utilizadas
- Python
- Flask
- JSON
- Threading (concurrencia)
- Visual Studio Code

---

## 🔥 Funcionalidades

### 👤 Usuarios
- Registrar usuario
- Listar usuarios

### 📦 Productos
- Agregar productos
- Listar productos

### 🛒 Carrito
- Agregar productos
- Ver carrito
- Eliminar productos

### 💰 Ventas
- Realizar compra
- Calcular total

---

## 🌐 Servicios Web (API)

| Método | Endpoint | Descripción |
|--------|----------|------------|
| POST | /usuarios | Registrar usuario |
| GET | /usuarios | Listar usuarios |
| POST | /productos | Crear producto |
| GET | /productos | Ver productos |
| POST | /carrito | Agregar al carrito |
| GET | /carrito | Ver carrito |
| DELETE | /carrito | Eliminar producto |
| POST | /ventas | Realizar compra |

---

## ⚡ Concurrencia
Se implementó concurrencia mediante `threading`, permitiendo procesar ventas en segundo plano sin bloquear el sistema.

---

## 📦 Ejemplo de uso

### Crear usuario
```json
POST /usuarios
{
  "nombre": "Andy",
  "correo": "andy@mail.com"
}
