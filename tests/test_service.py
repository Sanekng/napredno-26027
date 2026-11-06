from decimal import Decimal

from models import Reservation
from reports import ReportWriter
from service import ReservationService
from sources import MemoryReservationSource


class MemoryReportWriter:
    def __init__(self):
        self.amounts = None

    def write(self, amounts):
        self.amounts = list(amounts)


def create_service(reservations):
    writer: ReportWriter = MemoryReportWriter()
    service = ReservationService(MemoryReservationSource(reservations), writer)
    return service, writer


def test_process_calculates_reservations_and_generates_report():
    service, writer = create_service(
        [
            Reservation("Ana", 2, Decimal("25.00")),
            Reservation("Marko", 3, Decimal("10.00")),
        ]
    )

    amounts = service.process()

    assert amounts == [Decimal("50.00"), Decimal("30.00")]
    assert writer.amounts == amounts


def test_total_amount_is_calculated_correctly():
    service, _ = create_service([])

    assert service.total_amount([Decimal("50.00"), Decimal("30.00")]) == Decimal("80.00")


def test_empty_reservation_list_generates_empty_report():
    service, writer = create_service([])

    assert service.process() == []
    assert writer.amounts == []
