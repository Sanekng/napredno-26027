from pathlib import Path
import sys

from reports import TextReportWriter
from service import ReservationService
from sources import CsvReservationSource


def main() -> None:
    """Run reservation processing from a CSV file."""
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rezervacije.csv")
    service = ReservationService(
        CsvReservationSource(csv_path),
        TextReportWriter("izvjestaj.txt"),
    )
    service.process()


if __name__ == "__main__":
    main()