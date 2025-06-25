from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        mood = request.form.get('mood', '')
        mood_lower = mood.lower()
        if any(word in mood_lower for word in ('feliz', 'bien', 'contento')):
            message = 'Me alegra escuchar que te sientes bien!'
        elif any(word in mood_lower for word in ('triste', 'mal')):
            message = 'Lamento que te sientas así. Estoy aquí para escucharte.'
        else:
            message = 'Gracias por compartir cómo te sientes.'
    return render_template('index.html', message=message)
