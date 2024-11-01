import requests

def hae_vitsi():
    pyynto = "https://api.chucknorris.io/jokes/random"
    r = requests.get(pyynto).json()
    joke = r["value"]
    print(joke)

hae_vitsi()