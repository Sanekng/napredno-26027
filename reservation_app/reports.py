from decimal import Decimal
from pathlib import Path
from typing import Protocol, Sequence


class ReportWriter(Protocol):
    def write(self, amounts: Sequence[Decimal]) -> None:
        """Write a report for the calculated reservation amounts."""


class TextReportWriter:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def write(self, amounts: Sequence[Decimal]) -> None:
        values = ", ".join(f"{amount:.2f}" for amount in amounts)
        total = sum(amounts, Decimal("0"))
        report = f"Iznosi: [{values}]\nUkupno: {total:.2f}\n"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(report, encoding="utf-8")
        print("Poslato:", total)
