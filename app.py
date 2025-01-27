from resources.performers_api import performers_api as performers_ns
from resources.shows_api import shows_api as shows_ns
from resources.tickets_api import tickets_api as tickets_ns
import logging
from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, request, jsonify
from flask_restx import Api

app = Flask(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("standup_comedy_api")

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Информация о приложении Stand-Up Comedy", version="1.0")

api = Api(app, title="Stand-Up Comedy API", version="1.0", description="API для управления стендап-шоу")

# Добавляем пространства имен
api.add_namespace(performers_ns, path="/performers")
api.add_namespace(shows_ns, path="/shows")
api.add_namespace(tickets_ns, path="/tickets")

@app.route("/health", methods=["GET"])
def health():
    logger.info("Health check endpoint called")
    return jsonify({"status": "ok"})

@app.route("/test", methods=["GET"])
def test_logging():
    logger.debug("Received a request to /test endpoint with query params: %s", request.args)
    try:
        test_param = request.args.get("param", None)
        if not test_param:
            logger.warning("Missing 'param' query parameter in /test endpoint request")
            return jsonify({"error": "Missing 'param' query parameter"}), 400

        logger.info("Processing request with param: %s", test_param)
        if test_param == "error":
            logger.error("Simulated error triggered")
            raise ValueError("Simulated error")

        logger.info("Successfully processed request")
        return jsonify({"message": f"Test successful with param: {test_param}"}), 200
    except Exception as e:
        logger.critical("Critical error occurred in /test endpoint: %s", str(e))
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    logger.info("Starting Stand-Up Comedy API...")
    try:
        app.run(debug=True)
    except Exception as e:
        logger.critical("Failed to start application: %s", str(e))
