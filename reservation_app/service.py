from decimal import Decimal
from typing import Sequence

from .models import Reservation
from .reports import ReportWriter
from .sources import ReservationSource


class ReservationService:
    """Coordinates loading reservations, calculating amounts and reporting."""

    def __init__(self, source: ReservationSource, report_writer: ReportWriter):
        self.source = source
        self.report_writer = report_writer

    def process(self) -> list[Decimal]:
        reservations = self.source.load()
        amounts = [self.calculate_amount(reservation) for reservation in reservations]
        self.report_writer.write(amounts)
        return amounts

    @staticmethod
    def calculate_amount(reservation: Reservation) -> Decimal:
        return reservation.amount()

    @staticmethod
    def total_amount(amounts: Sequence[Decimal]) -> Decimal:
        return sum(amounts, Decimal("0"))
