from prometheus_client import Counter
from flask_restx import Namespace, Resource, fields
from services.performer_service import PerformerService
from flask import Blueprint, jsonify, request

performers_api = Namespace("Performers", description="Операции с артистами")

performer_model = performers_api.model("Performer", {
    "performer_id": fields.Integer(readOnly=True, description="ID артиста"),
    "name": fields.String(required=True, description="Имя артиста"),
    "bio": fields.String(required=True, description="Биография артиста"),
    "rating": fields.Float(required=True, description="Рейтинг артиста")
})

@performers_api.route("/")
class PerformerList(Resource):
    @performers_api.marshal_list_with(performer_model)
    def get(self):
        """Получить список артистов"""
        return PerformerService.get_all()

    @performers_api.expect(performer_model, validate=True)
    def post(self):
        """Добавить нового артиста"""
        return PerformerService.create(performers_api.payload), 201

# Создаём Blueprint
performers_bp = Blueprint("performers", __name__, url_prefix="/performers")

# Экземпляр PerformerService
performer_service = PerformerService()

# Счётчик запросов для метрики
performer_requests_total = Counter(
    "performer_requests_total", "Общее количество запросов к /performers"
)

# Маршрут для получения списка артистов
@performers_bp.route("/", methods=["GET"])
def get_performers():
    performer_requests_total.inc()  # Увеличиваем счётчик запросов
    performers = performer_service.get_all_performers()
    return jsonify({"performers": performers})

# Маршрут для добавления нового артиста
@performers_bp.route("/", methods=["POST"])
def add_performer():
    data = request.json
    new_performer = performer_service.add_performer(data)
    return jsonify(new_performer), 201
