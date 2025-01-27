from models.show import Show

class ShowService:
    _shows = [
        Show(1, 1, "2025-02-01T20:00:00", "Клуб Комедии"),
        Show(2, 2, "2025-02-02T18:00:00", "Театр Трагедии")
    ]

    @classmethod
    def get_all(cls):
        return [show.to_dict() for show in cls._shows]
