# Obrada rezervacija

Program učitava rezervacije iz CSV datoteke, računa iznos svake rezervacije
(broj noćenja * cijena po noćenju) i čuva tekstualni izvještaj.

## Struktura projekta

- `obrada.py` - pokretanje programa.
- `reservation_app/` - Python paket sa kodom aplikacije:
  - `models.py` - klasa `Reservation`.
  - `sources.py` - CSV izvor, memorijski izvor i `ReservationSource` protokol.
  - `reports.py` - `TextReportWriter` i `ReportWriter` protokol.
  - `service.py` - `ReservationService`, koji koordinira obradu.
- `data/rezervacije.csv` - primjer ulaznih podataka.
- `output/` - direktorij za generisani izvještaj.
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

Program zapisuje `output/izvjestaj.txt`. Ako se putanja ne navede, koristi
`data/rezervacije.csv`. Podrazumijevane putanje se računaju u odnosu na
direktorij projekta, pa se program može pokrenuti i iz drugog direktorija.

Za pokretanje sa primjerom:

```text
python obrada.py
```

## Testovi

```text
pytest
```

Testovi koriste `MemoryReservationSource`, pa za testiranje nije potrebna
stvarna CSV datoteka. Isti `ReservationService` radi i sa CSV i sa memorijskim
izvorom.

Testovi se mogu pokrenuti i direktno:

```text
python tests/test_service.py
```

## AI usage

AI je korišten kao pomoć pri refaktoriranju koda i pisanju testova.

Originalni kod je podijeljen u manje klase. Dodani su Protocol interfejsi i testovi koji koriste alternativni izvor podataka.

Pregledao sam generisani kod i napravio izmjene kako bi bio jednostavniji i razumljiviji.
