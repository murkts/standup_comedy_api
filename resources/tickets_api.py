from flask_restx import Namespace, Resource, fields
tickets_api = Namespace("Tickets", description="Операции с билетами")
ticket_model = tickets_api.model(
    "Ticket",
    {
        "id": fields.Integer(required=True, description="ID билета"),
        "show_id": fields.Integer(required=True, description="ID выступления"),
        "price": fields.Float(required=True, description="Цена билета"),
        "seat": fields.String(required=True, description="Место"),
    },
)
tickets = []


@tickets_api.route("/")
class TicketList(Resource):
    @tickets_api.marshal_list_with(ticket_model)
    def get(self):
        """Получить список всех билетов"""
        return tickets

    @tickets_api.expect(ticket_model)
    @tickets_api.response(201, "Билет успешно добавлен")
    def post(self):
        """Добавить новый билет"""
        new_ticket = tickets_api.payload
        new_ticket["id"] = len(tickets) + 1
        tickets.append(new_ticket)
        return {"message": "Билет добавлен", "ticket": new_ticket}, 201


@tickets_api.route("/<int:ticket_id>")
@tickets_api.param("ticket_id", "ID билета")
class Ticket(Resource):
    @tickets_api.marshal_with(ticket_model)
    @tickets_api.response(404, "Билет не найден")
    def get(self, ticket_id):
        """Получить билет по ID"""
        ticket = next((t for t in tickets if t["id"] == ticket_id), None)
        if ticket is None:
            tickets_api.abort(404, f"Билет с ID {ticket_id} не найден")
        return ticket

    @tickets_api.response(204, "Билет успешно удален")
    def delete(self, ticket_id):
        """Удалить билет по ID"""
        global tickets
        tickets = [t for t in tickets if t["id"] != ticket_id]
        return {"message": f"Билет с ID {ticket_id} удален"}, 204
