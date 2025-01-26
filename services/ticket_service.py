from models.ticket import Ticket

class TicketService:
    def __init__(self):
        self.tickets = []

    def purchase_ticket(self, data):
        ticket_id = len(self.tickets) + 1
        new_ticket = Ticket(ticket_id, data['show_id'], data['user_id'], data['seat_number'], data['price'])
        self.tickets.append(new_ticket)
        return new_ticket
