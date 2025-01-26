from flask import Blueprint, jsonify, request
from services.show_service import ShowService
from flasgger import swag_from

shows_bp = Blueprint('shows', __name__)

show_service = ShowService()

@shows_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Shows'],
    'summary': 'Получить расписание выступлений',
    'parameters': [
        {'name': 'performer_id', 'in': 'query', 'description': 'ID артиста', 'schema': {'type': 'integer'}},
        {'name': 'date', 'in': 'query', 'description': 'Дата выступления', 'schema': {'type': 'string', 'format': 'date'}},
        {'name': 'venue', 'in': 'query', 'description': 'Место проведения', 'schema': {'type': 'string'}}
    ],
    'responses': {
        '200': {
            'description': 'Расписание выступлений',
            'content': {
                'application/json': {
                    'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Show'}}
                }
            }
        }
    }
})
def get_shows():
    shows = show_service.get_shows()
    return jsonify([show.to_dict() for show in shows])

@shows_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Shows'],
    'summary': 'Добавить новое выступление',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {'$ref': '#/components/schemas/ShowCreation'}
            }
        }
    },
    'responses': {'201': {'description': 'Выступление успешно добавлено'}}
})
def add_show():
    data = request.get_json()
    new_show = show_service.add_show(data)
    return jsonify(new_show.to_dict()), 201
