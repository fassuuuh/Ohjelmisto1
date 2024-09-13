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

maakoodi = input("Syötä maakoodi: ").upper()

def print_countries(maakoodi):
    sql = f"SELECT type FROM airport WHERE iso_country = '{maakoodi}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    isot_lentokentat = 0
    pienet_lentokentat = 0
    helikopteri = 0
    medium = 0
    suljettu = 0
    if cursor.rowcount > 0:
        for row in result:
            if row[0] == "large_airport":
                isot_lentokentat += 1
            elif row[0] == "small_airport":
                pienet_lentokentat += 1
            elif row[0] == "heliport":
                helikopteri += 1
            elif row[0] == "medium_airport":
                medium += 1
            elif row[0] == "closed":
                suljettu += 1
        print(f"Isoja lentokenttiä on {isot_lentokentat}.")
        print(f"Pieniä lentokenttiä on {pienet_lentokentat}.")
        print(f"Helikopteri-lentokenttiä on {helikopteri}.")
        print(f"Keskikokoisia lentokenttiä on {medium}.")
        print(f"Suljettuja lentokenttiä on {suljettu}.")
        return

print_countries(maakoodi)
