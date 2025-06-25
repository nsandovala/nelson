# HEO – Human Emotion Optimization

Este proyecto contiene una aplicación Flask sencilla que actúa como un asistente emocional.

## Requisitos
- Python 3.10 o superior
- Flask

Puedes instalar las dependencias en un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usar: venv\Scripts\activate
pip install flask
```

## Ejecución

Establece la variable `FLASK_APP` y ejecuta el servidor:

```bash
export FLASK_APP=main.py
flask run
```

Luego abre `http://127.0.0.1:5000/` en tu navegador. Verás un mensaje de bienvenida y un formulario para indicar cómo te sientes.

## Uso en Visual Studio Code

1. Abre la carpeta del proyecto en VS Code.
2. Asegúrate de seleccionar el intérprete de Python correcto.
3. Ejecuta los comandos anteriores en el terminal integrado.
