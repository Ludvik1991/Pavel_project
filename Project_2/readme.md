## Domácí úkol – Open-Meteo API

Vybral jsem si open meteo API.
Pomocí Pythonu jsem si stáhl data o počasí pro Drahany a potom jsem je uložil do CSV souboru.  
Nakonec jsem z těchto dat udělal graf teploty pomocí knihovny Plotly.

## CO program dělá

Program stáhne hodinová data o počasí pro zadané místo.  
Konkrétně získá:

- čas
- teplotu
- vlhkost vzduchu
- rychlost větru

Potom tato data uloží do tabulky a exportuje do souboru `open_meteo_data.csv`.

Zároveň vytvoří graf teploty a uloží ho do souboru `open_meteo_graf.html`.

## Jaké knihovny jsem použil

V programu jsem použil tyto knihovny:

- `requests` – pro načtení dat z API
- `pandas` – pro práci s tabulkou
- `plotly` – pro vytvoření grafu

