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

icao = input("Syötä lentoaseman ICAO-koodi: ").upper()

def print_countries(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += f" WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Lentoaseman nimi on {row[0]} ja se on sijaintikunnassa {row[1]}")
        return

print_countries(icao)
