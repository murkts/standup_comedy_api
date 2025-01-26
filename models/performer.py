class Performer:
    def __init__(self, performer_id, name, bio, rating):
        self.performer_id = performer_id
        self.name = name
        self.bio = bio
        self.rating = rating

    def to_dict(self):
        return {
            'performer_id': self.performer_id,
            'name': self.name,
            'bio': self.bio,
            'rating': self.rating
        }
