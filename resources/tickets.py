from flask_restx import Namespace, Resource, fields
from services.ticket_service import TicketService

api = Namespace("Tickets", description="Операции с билетами")

ticket_model = api.model("Ticket", {
    "ticket_id": fields.Integer(readOnly=True, description="ID билета"),
    "show_id": fields.Integer(required=True, description="ID шоу"),
    "user_id": fields.Integer(required=True, description="ID пользователя"),
    "seat_number": fields.String(required=True, description="Номер места"),
    "price": fields.Float(required=True, description="Цена билета")
})

@api.route("/")
class TicketList(Resource):
    @api.marshal_list_with(ticket_model)
    def get(self):
        """Получить список всех билетов"""
        return TicketService.get_all()

    @api.expect(ticket_model, validate=True)
    def post(self):
        """Добавить новый билет"""
        return TicketService.create(api.payload), 201


@api.route("/<int:ticket_id>")
@api.param("ticket_id", "ID билета")
class Ticket(Resource):
    @api.marshal_with(ticket_model)
    def get(self, ticket_id):
        """Получить информацию о конкретном билете"""
        ticket = TicketService.get_by_id(ticket_id)
        if not ticket:
            api.abort(404, f"Билет с ID {ticket_id} не найден")
        return ticket

    def delete(self, ticket_id):
        """Удалить билет"""
        if TicketService.delete(ticket_id):
            return {"message": f"Билет с ID {ticket_id} удалён"}, 200
        api.abort(404, f"Билет с ID {ticket_id} не найден")
