from flask import Flask
from flask_restx import Api
from resources.performers import api as performers_ns
from resources.shows import api as shows_ns
from resources.tickets import api as tickets_ns

app = Flask(__name__)
api = Api(app, title="Stand-Up Comedy API", version="1.0", description="API для управления стендап-шоу")

api.add_namespace(performers_ns, path="/performers")
api.add_namespace(shows_ns, path="/shows")
api.add_namespace(tickets_ns, path="/tickets")

if __name__ == "__main__":
    app.run(debug=True)
