from flask import Flask, jsonify
import math

app = Flask(__name__)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/alkuluku/<int:luku>', methods=['GET'])
def alkuluku(luku):
    onko_alkuluku = is_prime(luku)

    vastaus = {
        "Number": luku,
        "isPrime": onko_alkuluku
    }

    return jsonify(vastaus)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
