from flask import Blueprint, jsonify, request
from services.ticket_service import TicketService
from flasgger import swag_from

tickets_bp = Blueprint('tickets', __name__)

ticket_service = TicketService()

@tickets_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Tickets'],
    'summary': 'Купить билет на выступление',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {'$ref': '#/components/schemas/TicketPurchase'}
            }
        }
    },
    'responses': {'201': {'description': 'Билет успешно куплен'}}
})
def purchase_ticket():
    data = request.get_json()
    new_ticket = ticket_service.purchase_ticket(data)
    return jsonify(new_ticket.to_dict()), 201
