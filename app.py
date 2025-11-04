from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env if present
load_dotenv()

app = Flask(__name__)
# Instantiate the OpenAI client using the latest library API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            try:
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Eres HEO, un asistente médico empático y preciso. "
                                "Responde con claridad y humanidad."
                            ),
                        },
                        {"role": "user", "content": user_input},
                    ],
                )
                response = completion.choices[0].message.content.strip()
            except Exception as exc:
                response = f"Error al conectar con HEO: {exc}"
    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)
