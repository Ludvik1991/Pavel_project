#naimportuju si potřebné knihovny pro aplikaci.
import requests
import pandas as pd
import plotly.express as px

# Souřadnice Drahany.
zemepisna_sirka = 49.4333
zemepisna_delka = 16.8974

# Adresa  API Open-Meteo
url = "https://api.open-meteo.com/v1/forecast"

# Požadavek
parametry = {
    "latitude": zemepisna_sirka,
    "longitude": zemepisna_delka,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "forecast_days": 3,
    "timezone": "auto"
}

# Odeslání požadavku
odpoved = requests.get(url, params=parametry)
odpoved.raise_for_status()

# Převod odpovědi na JSON
data = odpoved.json()

# Vytvoření tabulky, struktura tabulky, teplota v +2m, vlhkost +2m, +10m rychlost větru.
tabulka = pd.DataFrame({
    "cas": data["hourly"]["time"],
    "teplota_2m": data["hourly"]["temperature_2m"],
    "relativni_vlhkost_2m": data["hourly"]["relative_humidity_2m"],
    "rychlost_vetru_10m": data["hourly"]["wind_speed_10m"]
})

# Převod času na datetime
tabulka["cas"] = pd.to_datetime(tabulka["cas"])

# Uložení do CSV
tabulka.to_csv("open_meteo_data.csv", index=False, encoding="utf-8")

# Graf teploty
graf = px.line(
    tabulka,
    x="cas",
    y="teplota_2m",
    title="Předpověď teploty v Drahanech z Open-Meteo API",
    labels={
        "cas": "Čas",
        "teplota_2m": "Teplota (°C)"
    }
)

# Uložení grafu do HTML
graf.write_html("open_meteo_graf.html")

# Zobrazení grafu
graf.show()

print("Hotovo. Data byla uložena do open_meteo_data.csv a graf do open_meteo_graf.html")