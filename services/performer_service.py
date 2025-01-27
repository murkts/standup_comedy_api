from models.performer import Performer

class PerformerService:
    _performers = [
        Performer(1, "Сергей Орлов", "Комик с многолетним опытом", 4.5),
        Performer(2, "Виктория Складчикова", "Гений, миллиардер, филантроп", 4.0)
    ]

    @classmethod
    def get_all(cls):
        return [performer.to_dict() for performer in cls._performers]

    @classmethod
    def create(cls, data):
        new_id = len(cls._performers) + 1
        new_performer = Performer(new_id, data["name"], data["bio"], data["rating"])
        cls._performers.append(new_performer)
        return new_performer.to_dict()
