from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Reservation:
    """One reservation read from the input data."""

    guest: str
    nights: int
    price_per_night: Decimal

    def amount(self) -> Decimal:
        return Decimal(self.nights) * self.price_per_night
