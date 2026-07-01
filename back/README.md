# API REST Calculadora

Este proyecto implementa una calculadora web sencilla utilizando una **API REST desarrollada con FastAPI** y una **interfaz web básica** construida con HTML, CSS y JavaScript. 

El objetivo principal es ilustrar el funcionamiento de la **comunicación mediante mensajes entre un cliente y un servidor** bajo una arquitectura moderna.

---

## 🏗️ Arquitectura del Sistema

El proyecto está dividido físicamente en dos directorios para desacoplar la lógica:

* **`back/` (Backend):** Implementado con FastAPI en Python. Expone los servicios HTTP para realizar operaciones aritméticas (suma, resta, multiplicación, división, potencia, raíz cuadrada y valor absoluto).
* **`front/` (Frontend):** Aplicación web que permite introducir números, seleccionar una operación y visualizar el resultado comunicándose con el backend mediante la API fetch de JavaScript.

---

## 🛠️ Requisitos Previos

* Python 3
* pip (Gestor de paquetes de Python)
* Navegador Web (Safari, Chrome, Firefox, etc.)

---

## 🚀 Guía de Ejecución Paso a Paso

Para ejecutar el sistema completo, se requiere iniciar tanto el backend como el frontend de manera simultánea en **dos terminales diferentes**.

### PASO 1: Ejecutar el Backend (API REST)

Abre tu terminal, colócate en la raíz del proyecto y navega hacia la carpeta del servidor:
`cd back`

**1. Crear el entorno virtual**
`python3 -m venv .venv`

**2. Activar el entorno virtual**
`source .venv/bin/activate`

**3. Instalar dependencias**
`pip install -r requirements.txt`

**4. Iniciar el servidor**
`uvicorn main:app --reload`

**🌐 Enlaces del Backend:**
* Servidor principal: http://localhost:8000
* Documentación API (Swagger UI): http://localhost:8000/docs

### PASO 2: Ejecutar el Frontend (Interfaz Web)

Abre una **nueva terminal**, ve a la raíz del proyecto y entra a la carpeta del cliente:
`cd front`

**1. Iniciar servidor web local**
`python3 -m http.server 5173`

**🌐 Enlace del Frontend:**
* Abre tu navegador y visita: http://localhost:5173

---

## 🔄 Flujo de Comunicación

El modelo de intercambio sigue esta ruta:
Frontend → HTTP Request (GET/POST) → API REST → Servicio → JSON Response → Frontend

1. El usuario introduce los datos numéricos y elige una operación.
2. JavaScript envía una solicitud HTTP al servidor local.
3. La API procesa la operación matemática.
4. El servidor devuelve una respuesta en formato JSON.
5. JavaScript decodifica el JSON y actualiza el resultado.

---

## 📡 Métodos HTTP (GET vs POST)

La API implementa dos mecanismos distintos para recibir datos:

### Operaciones Básicas (GET)
Los parámetros viajan expuestos en la URL.
* Petición de ejemplo: GET /api/add?a=5&b=3
* Respuesta esperada:
  {
    "operacion": "suma",
    "a": 5.0,
    "b": 3.0,
    "resultado": 8.0
  }

### Operaciones Avanzadas (POST)
Los datos viajan de manera estructurada dentro del cuerpo (body) de la petición.
* Petición de ejemplo: POST /api/power
* Cuerpo enviado:
  {
    "a": 2.0,
    "b": 3.0
  }
* Respuesta esperada:
  {
    "operacion": "potencia",
    "a": 2.0,
    "b": 3.0,
    "resultado": 8.0
  }