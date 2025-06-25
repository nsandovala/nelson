from flask import Blueprint, render_template, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    user_feeling = None
    response = None
    if request.method == 'POST':
        user_feeling = request.form.get('feeling', '')
        if any(word in user_feeling.lower() for word in ['bien', 'feliz', 'content']):
            response = 'Me alegra saber que te sientes bien!'
        elif any(word in user_feeling.lower() for word in ['mal', 'triste', 'deprim']):
            response = 'Lamento que te sientas así. Estoy aquí para ayudarte.'
        else:
            response = 'Gracias por compartir cómo te sientes.'
    return render_template('index.html', response=response)
