from models.show import Show

class ShowService:
    def __init__(self):
        self.shows = [
            Show(1001, 1, "2024-10-20T20:00:00", "Клуб Комедии"),
            Show(1002, 2, "2024-10-21T18:00:00", "Клуб Трагедии")
        ]

    def get_shows(self):
        return self.shows

    def add_show(self, data):
        new_show = Show(len(self.shows) + 1, data['performer_id'], data['date_time'], data['venue'])
        self.shows.append(new_show)
        return new_show
