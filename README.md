# Obrada rezervacija

Program učitava rezervacije iz CSV datoteke, računa iznos svake rezervacije
(broj noćenja * cijena po noćenju) i čuva tekstualni izvještaj.

## Struktura projekta

- `obrada.py` - pokretanje programa.
- `models.py` - klasa `Reservation`.
- `sources.py` - `CsvReservationSource`, memorijski izvor i `ReservationSource`
  protokol.
- `reports.py` - `TextReportWriter` i `ReportWriter` protokol.
- `service.py` - `ReservationService`, koji koordinira obradu.
- `tests/test_service.py` - pytest testovi.

CSV red ima oblik `ime,broj_noćenja,cijena_po_noćenju`, na primjer:

```text
Ana,2,25.00
Marko,3,10.00
```

## SRP, DIP i Protocol

Svaka klasa ima jednu glavnu odgovornost: izvor učitava podatke, servis računa
iznose, a izvještaj ih zapisuje. To je Single Responsibility Principle (SRP).

`ReservationService` dobija izvor i izvještaj kroz konstruktor. Ne pravi
konkretne objekte sam i zavisi od jednostavnih protokola, što primjenjuje
Dependency Inversion Principle (DIP). Zbog toga se novi izvor može dodati bez
izmjene servisa.

`ReservationSource` opisuje objekat koji ima `load()` metodu, a `ReportWriter`
opisuje objekat koji ima `write()` metodu. Python `Protocol` omogućava da
konkretne klase slijede ovaj dogovor bez nasljeđivanja.

## Pokretanje

Instalirajte pytest ako je potrebno:

```text
pip install -r requirements.txt
```

Pokrenite program sa CSV datotekom:

```text
python obrada.py rezervacije.csv
```

Program zapisuje `izvjestaj.txt` u trenutni direktorij. Ako se putanja ne
navede, koristi `rezervacije.csv`.

## Testovi

```text
pytest
```

Testovi koriste `MemoryReservationSource`, pa za testiranje nije potrebna
stvarna CSV datoteka. Isti `ReservationService` radi i sa CSV i sa
memorijskim izvorom.

## AI usage

Korišten je korisnički prompt za ovaj zadatak: “Mini Project 1 – Refactoring
Reservation Processing”, sa zahtjevima za refaktoriranje `obrada.py`, SRP,
DIP, Python `Protocol`, alternativni izvor, pytest testove i README.

Izvorni kod je bio jedna klasa koja je učitavala CSV, računala iznose, pisala
izvještaj i ispisivala ukupnu vrijednost. Kod je razdvojen u modele, izvore,
izvještaj i servis. Dodati su konstruktorom proslijeđeni zavisni objekti,
memorijski izvor i tri testa. Iznosi koriste `Decimal`, a `obrada.py` je
zadržan kao ulazna tačka programa.
