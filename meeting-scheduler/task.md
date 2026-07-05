# Meeting Management System

---

## 🇵🇱 Opis

Celem zadania jest implementacja systemu zarządzania spotkaniami z obsługą stref czasowych.  
System umożliwia filtrowanie, grupowanie oraz eksport danych do plików tekstowych.

---

## Model danych

### Meeting

Każde spotkanie zawiera:

- `meeting_id` – identyfikator
- `description` – opis
- `meeting_datetime` – data i czas (timezone-aware)

Założenia:
- brak czasu trwania (pojedynczy punkt w czasie)
- wszystkie operacje uwzględniają strefy czasowe

---

## Funkcjonalności

### a) Nadchodzące spotkania
- spotkania w przyszłości
- sortowanie rosnąco po czasie

---

### b) Dzisiejsze spotkania
- spotkania z bieżącego dnia
- porównanie w lokalnej strefie systemu

---

### c) Archiwalne spotkania
- zapis do pliku `.txt`
- tylko spotkania już zakończone

---

### d) Grupowanie spotkań
- grupowanie po dniu kalendarzowym
- oraz godzinie rozpoczęcia
- eksport do pliku `.txt`

---

## Strefy czasowe

- system obsługuje różne strefy czasowe
- wszystkie porównania wymagają normalizacji czasu

---

## Reguły

- dane wejściowe są niemutowalne
- brak wyników → pusta lista / pusty plik
- spójne operacje na czasie

---

## Struktura

- `meeting.py` – model danych
- `service.py` – logika biznesowa
- `file_handler.py` – zapis do plików
- `run.py` – punkt wejścia
- `data.json` – dane przykładowe

---

## 🇬🇧 Description

The goal of this task is to implement a meeting management system with timezone support.  
The system allows filtering, grouping, and exporting meeting data to text files.

---

## Data model

### Meeting

Each meeting contains:

- `meeting_id` – identifier
- `description` – description
- `meeting_datetime` – timezone-aware datetime

Assumptions:
- no duration (single timestamp)
- all operations must respect timezones

---

## Features

### a) Upcoming meetings
- meetings in the future
- sorted ascending by datetime

---

### b) Today’s meetings
- meetings occurring on the current calendar day
- comparison in system local timezone

---

### c) Past meetings
- exported to `.txt`
- only meetings already completed

---

### d) Grouped meetings
- grouped by calendar day
- and start hour
- exported to `.txt`

---

## Timezones

- system supports multiple timezones
- all comparisons require normalization

---

## Rules

- input data is immutable
- empty result → empty list / empty file
- consistent time-based operations

---

## Structure

- `meeting.py` – data model
- `service.py` – business logic
- `file_handler.py` – file export
- `run.py` – entry point
- `data.json` – sample data