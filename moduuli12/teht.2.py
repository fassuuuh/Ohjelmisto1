import requests

def hae_saa(kaupunki):
    pyynto = (f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid=eff20526b7278e15d4a5aa12b50b725a&units=metric&lang=fi")
    r = requests.get(pyynto).json()
    weather = r["weather"][0]["description"]
    temperature = r["main"]["temp"]
    print(weather)
    print(f"{temperature:.1f} astetta")

kaupunki = input("Syötä kaupunki: ")
hae_saa(kaupunki)
