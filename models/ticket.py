class Ticket:
    def __init__(self, ticket_id, show_id, user_id, seat_number, price):
        self.ticket_id = ticket_id
        self.show_id = show_id
        self.user_id = user_id
        self.seat_number = seat_number
        self.price = price

    def to_dict(self):
        return {
            'ticket_id': self.ticket_id,
            'show_id': self.show_id,
            'user_id': self.user_id,
            'seat_number': self.seat_number,
            'price': self.price
        }
