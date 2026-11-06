import csv
from decimal import Decimal
from pathlib import Path
from typing import Protocol

from models import Reservation


class ReservationSource(Protocol):
    def load(self) -> list[Reservation]:
        """Return all reservations available from this source."""


class CsvReservationSource:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def load(self) -> list[Reservation]:
        reservations: list[Reservation] = []
        with self.path.open(newline="", encoding="utf-8") as file:
            for row in csv.reader(file):
                reservations.append(
                    Reservation(row[0], int(row[1]), self._price(row[2]))
                )
        return reservations

    @staticmethod
    def _price(value: str) -> Decimal:
        return Decimal(value)


class MemoryReservationSource:
    """A source useful for tests and small examples."""

    def __init__(self, reservations: list[Reservation]):
        self.reservations = reservations

    def load(self) -> list[Reservation]:
        return self.reservations
