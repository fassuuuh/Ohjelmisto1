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
def print_countries():
    cursor = connection.cursor()
    cursor.execute('SELECT name, iso_country FROM country')
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount == 0:
        print("Ei yhtään maita.")
    else:
        for row in result:
            print(f"Maan {row[0]} maakoodi on {row[1]}.")
        print(f"Maita yhteensä: {cursor.rowcount}.")

print_countries()

def add_country(code, name):
    sql = f"INSERT INTO country VALUES ('{code}', '{name}', null, null, null)"
    cursor = connection.cursor()
    cursor.execute(sql)
    print(cursor.rowcount)

country_name = input("Anna lisättävän Maan nimi: ")
country_code = input("Anna lisättävän maan koodi: ")
add_country(country_code, country_name)

