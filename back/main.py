import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class OperacionRequest (BaseModel):
    a: float
    b: float

# -------------------------------------------------------
# Creación de la aplicación
# -------------------------------------------------------
# FastAPI es el framework que nos permite crear servicios
# web que se comunican mediante mensajes HTTP.
app = FastAPI(
    title="API REST - Calculadora",
    description="API sencilla para realizar operaciones aritméticas básicas",
    version="1.0"
)

# -------------------------------------------------------
# Configuración de CORS
# -------------------------------------------------------
# CORS (Cross-Origin Resource Sharing) permite que
# aplicaciones web ejecutándose en otros puertos puedan
# consumir esta API.
#
# En desarrollo es común que el frontend se ejecute en
# otro puerto distinto al backend.
allowed_origins = [
    "http://localhost:5173",  # acceso 1
    "http://localhost:3000",  # acceso 2
    "http://localhost:4200"   # acceso 3
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    max_age=600
)

# -------------------------------------------------------
# Servicios de la calculadora
# -------------------------------------------------------
# En una arquitectura real, esta lógica se colocaría en
# archivos separados llamados "services".
# Aquí se mantienen en el mismo archivo para simplificar
# el ejemplo para fines educativos.



def suma(a: float, b: float):
    """Realiza la suma de dos números."""
    return a + b


def resta(a: float, b: float):
    """Realiza la resta de dos números."""
    return a - b


def multiplicacion(a: float, b: float):
    """Realiza la multiplicación de dos números."""
    return a * b


def division(a: float, b: float):
    """Realiza la división de dos números."""
    if b == 0:
       return None
    return a / b


# -------------------------------------------------------
# Endpoints de la API
# -------------------------------------------------------
# Cada endpoint representa un servicio que recibe un
# mensaje HTTP, ejecuta una operación y devuelve
# una respuesta en formato JSON.


@app.get("/api/add")
def add(a: float, b: float):
    resultado = suma(a, b)

    return {
        "operacion": "suma",
        "a": a,
        "b": b,
        "resultado": resultado
    }


@app.get("/api/subtract")
def subtract(a: float, b: float):
    resultado = resta(a, b)

    return {
        "operacion": "resta",
        "a": a,
        "b": b,
        "resultado": resultado
    }


@app.get("/api/multiply")
def multiply(a: float, b: float):
    resultado = multiplicacion(a, b)

    return {
        "operacion": "multiplicacion",
        "a": a,
        "b": b,
        "resultado": resultado
    }


@app.get("/api/divide")
def divide(a: float, b: float):

    resultado = division(a, b)

    if resultado is None:
        return {
            "error": "No es posible dividir entre cero"
        }

    return {
        "operacion": "division",
        "a": a,
        "b": b,
        "resultado": resultado
    }


@app.post("/api/power")
def power(datos: OperacionRequest):
    resultado = datos.a ** datos.b

    return {
	"operacion": "potencia",
	"a": datos.a,
	"b": datos.b,
	"resultado": resultado

    }


@app.post("/api/sqrt")
def sqrt(datos: OperacionRequest):
    resultado = datos.a ** 0.5

    return {
	"operacion": "raiz cuadrada",
	"a": datos.a,
	"resultado": resultado

    }


@app.post("/api/calcular_abs")
def calcular_abs(datos: OperacionRequest):
    if datos.a < 0:
        resultado = datos.a * -1
    else:
        resultado = datos.a
        
    return {
        "operacion": "valor absoluto",
        "a": datos.a,
        "resultado": resultado
    }
