# Notes / Notatki

## 🇵🇱 Sposób obliczania ceny

Cena końcowa produktu liczona jest w dwóch krokach:

1. Najpierw do ceny bazowej doliczany jest podatek:
   - `price + (price * tax)`

2. Następnie, jeśli aktualny dzień znajduje się w zbiorze dni zniżkowych,
   do wyniku stosowana jest zniżka procentowa:
   - `final_price * (1 - discount)`

Zniżka jest stosowana po doliczeniu podatku.

### Założenia projektowe
- dzień tygodnia jest stanem obiektu (`_current_day`)
- brak ustawienia dnia oznacza domyślnie dzień `0`
- `discount_days` definiuje stałą konfigurację produktu


### Separacja warstw
Logika biznesowa została całkowicie oddzielona od interfejsu użytkownika.
Klasy w solution.py nie wiedzą o istnieniu terminala czy plików JSON.

### Dynamiczne wczytywanie
Zastosowano moduł argparse, co pozwala na testowanie różnych scenariuszy cenowych bez edycji kodu źródłowego.
---

## 🇬🇧 Price calculation approach

Final price is calculated in two steps:

1. First, tax is applied to the base price:
   - `price + (price * tax)`

2. Then, if the current day is included in the discount days set,
   a percentage discount is applied:
   - `final_price * (1 - discount)`

Discount is applied after tax is included.

### Design assumptions
- weekday is stored as object state (`_current_day`)
- default day is `0` if not explicitly set
- `discount_days` defines static product configuration

### Separation of Concerns
Business logic is decoupled from the UI. 
Classes in solution.py are independent of terminal interactions or JSON parsing.

### Dynamic Loading
Implemented argparse to allow testing various pricing scenarios via external JSON files without modifying the source code.