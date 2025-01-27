from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask
from flask_restx import Api
from resources.performers_api import performers_api as performers_ns
from resources.shows_api import shows_api as shows_ns
from resources.tickets_api import tickets_api as tickets_ns

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Информация о приложении", version="1.0")

api = Api(
    app,
    title="Stand-Up Comedy API",
    version="1.0",
    description="API для управления стендап-шоу"
)

# Добавление пространств имен
api.add_namespace(performers_ns, path="/performers")
api.add_namespace(shows_ns, path="/shows")
api.add_namespace(tickets_ns, path="/tickets")

if __name__ == "__main__":
    app.run(debug=True)
