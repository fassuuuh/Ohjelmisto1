from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Tietokantayhteyden määrittely
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True,
    collation='utf8mb4_general_ci'
)


@app.route('/kenttä/<string:icao>', methods=['GET'])
def hae_kentta(icao):
    # SQL-kysely, joka hakee lentokentän nimen ja kaupungin ICAO-koodin perusteella
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        vastaus = {
            "ICAO": icao,
            "Name": result[0],
            "Municipality": result[1]
        }
    else:
        # Jos kenttää ei löydy, palautetaan viesti
        vastaus = {
            "message": f"Lentokenttää ICAO-koodilla {icao} ei löytynyt."
        }

    return jsonify(vastaus)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
