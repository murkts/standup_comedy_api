from models.performer import Performer

class PerformerService:
    def __init__(self):
        self.performers = [
            Performer(1, "Сергей Орлов", "Комик с многолетним опытом", 4.5),
            Performer(2, "Виктория Складчикова", "Гений, миллиардер, филантроп", 4.0)
        ]

    def get_performers(self):
        return self.performers

    def add_performer(self, data):
        new_performer = Performer(len(self.performers) + 1, data['name'], data['bio'], data['rating'])
        self.performers.append(new_performer)
        return new_performer
