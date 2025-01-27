from flask_restx import Namespace, Resource, fields
from services.show_service import ShowService

api = Namespace("Shows", description="Операции с выступлениями")

show_model = api.model("Show", {
    "show_id": fields.Integer(readOnly=True, description="ID выступления"),
    "performer_id": fields.Integer(required=True, description="ID артиста, участвующего в стенд-апе"),
    "date_time": fields.String(required=True, description="Дата и время выступления (ISO формат)"),
    "venue": fields.String(required=True, description="Место проведения стенд-апа")
})

@api.route("/")
class ShowList(Resource):
    @api.marshal_list_with(show_model)
    def get(self):
        """Получить список выступлений"""
        return ShowService.get_all()

    @api.expect(show_model, validate=True)
    def post(self):
        """Добавить новое выступление"""
        return ShowService.create(api.payload), 201


@api.route("/<int:show_id>")
@api.param("show_id", "ID выступления")
class Show(Resource):
    @api.marshal_with(show_model)
    def get(self, show_id):
        """Получить информацию о конкретном выступлении"""
        show = ShowService.get_by_id(show_id)
        if not show:
            api.abort(404, f"Выступление с ID {show_id} не найдено")
        return show

    def delete(self, show_id):
        """Удалить Выступление"""
        if ShowService.delete(show_id):
            return {"message": f"Выступление с ID {show_id} удалено"}, 200
        api.abort(404, f"Выступление с ID {show_id} не найдено")
