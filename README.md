# HEO - Human Emotion Optimization

Este proyecto proporciona una estructura básica con Flask para crear un asistente emocional.

## Requisitos

- Python 3.10+
- Flask

Instala las dependencias ejecutando:

```bash
pip install flask
```

## Estructura

```
heo_app/       # Código principal de la aplicación
templates/     # Plantillas Jinja2
static/        # Archivos estáticos (CSS)
main.py        # Punto de entrada
```

## Ejecución en Visual Studio Code

1. Abre la carpeta del proyecto en VS Code.
2. Crea un entorno virtual si lo deseas y actívalo.
3. Instala las dependencias con `pip install flask`.
4. Desde la terminal, ejecuta:

```bash
export FLASK_APP=main.py
flask run
```

Abre el navegador en `http://127.0.0.1:5000/` para ver la aplicación.

