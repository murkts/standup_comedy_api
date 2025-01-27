from flask_restx import Namespace, Resource

shows_api = Namespace("Shows", description="Операции с выступлениями")

@shows_api.route("/")
class ShowList(Resource):
    def get(self):
        return {"message": "Список всех выступлений"}

    def post(self):
        return {"message": "Добавить новое выступление"}

@shows_api.route("/<int:show_id>")
class Show(Resource):
    def get(self, show_id):
        return {"message": f"Получить информацию о шоу с ID {show_id}"}

    def delete(self, show_id):
        return {"message": f"Удалить шоу с ID {show_id}"}
