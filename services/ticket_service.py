from typing import List, Optional

class TicketService:
    _tickets = []
    _next_id = 1

    @classmethod
    def get_all(cls) -> List[dict]:
        """Получить список всех билетов."""
        return cls._tickets

    @classmethod
    def get_by_id(cls, ticket_id: int) -> Optional[dict]:
        """Получить билет по ID."""
        return next((ticket for ticket in cls._tickets if ticket["ticket_id"] == ticket_id), None)

    @classmethod
    def create(cls, data: dict) -> dict:
        """Создать новый билет."""
        ticket = {
            "ticket_id": cls._next_id,
            "show_id": data["show_id"],
            "user_id": data["user_id"],
            "seat_number": data["seat_number"],
            "price": data["price"]
        }
        cls._tickets.append(ticket)
        cls._next_id += 1
        return ticket

    @classmethod
    def delete(cls, ticket_id: int) -> bool:
        """Удалить билет по ID."""
        ticket = cls.get_by_id(ticket_id)
        if ticket:
            cls._tickets.remove(ticket)
            return True
        return False
