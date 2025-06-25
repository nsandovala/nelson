# HEO - Human Emotion Optimization

Este proyecto proporciona una base simple usando Flask para crear un asistente emocional llamado **HEO**.

## Requisitos

- Python 3.10 o superior
- Flask

Instala las dependencias con:

```bash
pip install flask
```

## Estructura del proyecto

- `main.py`: punto de entrada de la aplicación.
- `heo_app/`: módulo principal con la aplicación y las rutas.
- `templates/`: plantillas HTML con Jinja2.
- `static/`: archivos estáticos (CSS, imágenes, etc.).

## Uso

Desde Visual Studio Code o la terminal ejecuta:

```bash
flask --app main run
```

Luego abre [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador. Aparecerá una página con un saludo empático y un formulario para indicar cómo te sientes. Dependiendo del texto introducido, HEO responderá con un mensaje simple.


