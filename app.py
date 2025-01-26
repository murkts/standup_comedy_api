from flask import Flask
from flasgger import Swagger
from resources.performers import performers_bp
from resources.shows import shows_bp
from resources.tickets import tickets_bp

app = Flask(__name__)
Swagger(app)  # Инициализация Swagger для документации

# Регистрация Blueprint для ресурсов
app.register_blueprint(performers_bp, url_prefix='/performers')
app.register_blueprint(shows_bp, url_prefix='/shows')
app.register_blueprint(tickets_bp, url_prefix='/tickets')

@app.route('/')
def home():
    return "Welcome to the Stand-Up Comedy API! Use /performers, /shows, or /tickets to interact with the API."

if __name__ == "__main__":
    app.run(debug=True)
