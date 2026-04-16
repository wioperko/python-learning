# Product pricing system

---

## 🇵🇱 Opis

Celem tego zadania jest zbudowanie prostego systemu, który symuluje wyliczanie cen produktów z uwzględnieniem podatku oraz zniżek zależnych od dnia zakupu.

Model zakłada, że produkty mają cenę bazową, a końcowa kwota może być modyfikowana przez dodatkowe reguły biznesowe.

### Opis problemu

System powinien obsługiwać dwa typy produktów:

- podstawowy produkt, gdzie cena końcowa uwzględnia tylko podatek
- rozszerzony produkt, który może mieć zniżki w określone dni tygodnia

Dodatkowo należy umożliwić przetwarzanie listy zakupów i obliczenie całkowitej kwoty dla produktów kupionych w różnych dniach.

### Reguły biznesowe

- podatek zawsze wchodzi w skład ceny końcowej
- zniżki obowiązują tylko w wybrane dni tygodnia
- dni tygodnia są reprezentowane jako liczby od 0 do 6

### Cel implementacji

- poprawne modelowanie produktów i ich zachowań
- oddzielenie logiki cen od agregacji danych
- czytelne obliczanie ceny końcowej

---

## 🇬🇧 Description

The goal of this exercise is to build a simple system that simulates product pricing with support for tax calculation and time-based discounts.

The model assumes that products have a base price, and the final amount can be modified by additional business rules.

### Problem description

The system should support two types of products:

- a basic product where the final price includes only tax
- an extended product with discounts applied on specific days of the week

Additionally, the system should allow processing a list of purchases and calculating the total amount for products bought on different days.

### Business rules

- tax is always included in the final price
- discounts apply only on specific days of the week
- days are represented as integers from 0 to 6

### Implementation goals

- model products and their behavior correctly
- separate pricing logic from data aggregation
- implement clear and readable final price calculation