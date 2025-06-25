from flask import Flask, render_template, request

app = Flask(__name__)

# Simple sentiment detection based on keywords
POSITIVE_WORDS = {"bien", "feliz", "alegre", "contento", "excelente"}
NEGATIVE_WORDS = {"triste", "mal", "deprimido", "enojado", "horrible"}


def detect_sentiment(text: str) -> str:
    """Return 'positivo', 'negativo' or 'neutral' based on simple keyword search."""
    text = text.lower()
    if any(word in text for word in POSITIVE_WORDS):
        return "positivo"
    if any(word in text for word in NEGATIVE_WORDS):
        return "negativo"
    return "neutral"


@app.route("/", methods=["GET", "POST"])
def index():
    message = "Hola, soy HEO. ¿Cómo te sientes hoy?"
    response = None
    if request.method == "POST":
        feeling = request.form.get("feeling", "")
        sentiment = detect_sentiment(feeling)
        if sentiment == "positivo":
            response = "Me alegra saber que te sientes bien!"
        elif sentiment == "negativo":
            response = "Siento que no te sientas bien. Estoy aquí para escucharte."
        else:
            response = "Gracias por compartir cómo te sientes."
    return render_template("index.html", message=message, response=response)


if __name__ == "__main__":
    app.run(debug=True)
