from flask import Blueprint, jsonify, request
from services.performer_service import PerformerService
from flasgger import swag_from

performers_bp = Blueprint('performers', __name__)

performer_service = PerformerService()

@performers_bp.route('/', methods=['GET'])
@swag_from({
    'tags': ['Performers'],
    'summary': 'Получить список всех артистов',
    'parameters': [
        {'name': 'rating_min', 'in': 'query', 'description': 'Минимальный рейтинг артиста', 'schema': {'type': 'number', 'format': 'float'}},
        {'name': 'rating_max', 'in': 'query', 'description': 'Максимальный рейтинг артиста', 'schema': {'type': 'number', 'format': 'float'}},
        {'name': 'limit', 'in': 'query', 'description': 'Лимит записей на страницу', 'schema': {'type': 'integer'}},
        {'name': 'offset', 'in': 'query', 'description': 'Смещение записей', 'schema': {'type': 'integer'}}
    ],
    'responses': {
        '200': {
            'description': 'Список артистов',
            'content': {
                'application/json': {
                    'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Performer'}}
                }
            }
        }
    }
})
def get_performers():
    performers = performer_service.get_performers()
    return jsonify([performer.to_dict() for performer in performers])

@performers_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Performers'],
    'summary': 'Добавить нового артиста',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {'$ref': '#/components/schemas/PerformerCreation'}
            }
        }
    },
    'responses': {'201': {'description': 'Артист успешно добавлен'}}
})
def add_performer():
    data = request.get_json()
    new_performer = performer_service.add_performer(data)
    return jsonify(new_performer.to_dict()), 201
