# Aplicacaion de ejemplo en FastAPI

Esta aplicacion consiste en una API sencilla en la cual podemos almacenar valores relacionados a una etiqueta arbitraria, como un ejemplo de una API de gestion de parametros de una app, juego o sitio web.

## Inicio rapido
* Clonar el repositorio en una carpeta elegida por el usuario
* Crear entorno virtual de Python en la carpeta raiz
* Instalar redis
* Activar el entorno virtual usando: source bin/activate
* Instalar modulos de Python usando pip: pip install -r requirements.txt
* Ejecutar app mediante el comando: fastapi dev src/fastapi_demo/app.py

## Ejecutar codigo desde modulo instalado
* Desde la carpeta raiz con el entorno virtual activado
* Crear paquete/modulo de python mediante el comando python3 -m build
* Instalar uvicorn mediante pip install uvicorn
* Instalar paquete generado mediante pip install dist/<nombredepaquete>.whl
* Ejecutar el servidor mediante el comando uvicorn fastapi_demo:create_app