from flask_restx import Namespace, Resource, fields
from services.performer_service import PerformerService

api = Namespace("Performers", description="Операции с артистами")

performer_model = api.model("Performer", {
    "performer_id": fields.Integer(readOnly=True, description="ID артиста"),
    "name": fields.String(required=True, description="Имя артиста"),
    "bio": fields.String(required=True, description="Биография артиста"),
    "rating": fields.Float(required=True, description="Рейтинг артиста")
})

@api.route("/")
class PerformerList(Resource):
    @api.marshal_list_with(performer_model)
    def get(self):
        """Получить список артистов"""
        return PerformerService.get_all()

    @api.expect(performer_model, validate=True)
    def post(self):
        """Добавить нового артиста"""
        return PerformerService.create(api.payload), 201
