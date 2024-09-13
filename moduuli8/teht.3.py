from geopy import distance
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='salasana',
         autocommit=True,
         collation='utf8mb4_general_ci'
         )

def hae_koordinaatit(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

icao1 = input("Syötä 1. lentoaseman ICAO-koodi: ").upper()
icao2 = input("Syötä 2. lentoaseman ICAO-koodi: ").upper()

koordinaatit1 = hae_koordinaatit(icao1)
koordinaatit2 = hae_koordinaatit(icao2)

print(f"Etäisyys lentokenttien välillä on {distance.distance(koordinaatit1, koordinaatit2).km:.2f} kilometriä.")