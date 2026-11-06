from pathlib import Path
import sys

from reservation_app.reports import TextReportWriter
from reservation_app.service import ReservationService
from reservation_app.sources import CsvReservationSource


PROJECT_ROOT = Path(__file__).parent


def main() -> None:
    """Run reservation processing from a CSV file."""
    csv_path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else PROJECT_ROOT / "data" / "rezervacije.csv"
    )
    service = ReservationService(
        CsvReservationSource(csv_path),
        TextReportWriter(PROJECT_ROOT / "output" / "izvjestaj.txt"),
    )
    service.process()


if __name__ == "__main__":
    main()