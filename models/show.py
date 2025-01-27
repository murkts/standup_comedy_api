class Show:
    def __init__(self, show_id, performer_id, date_time, venue):
        self.show_id = show_id
        self.performer_id = performer_id
        self.date_time = date_time
        self.venue = venue

    def to_dict(self):
        return {
            "show_id": self.show_id,
            "performer_id": self.performer_id,
            "date_time": self.date_time,
            "venue": self.venue
        }
