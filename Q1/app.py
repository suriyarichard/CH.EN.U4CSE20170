from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_numbers_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "numbers" in data and isinstance(data["numbers"], list):
                return data["numbers"]
    except:
        pass
    return None

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    valid_numbers = []

    for url in urls:
        numbers = fetch_numbers_from_url(url)
        if numbers is not None:
            valid_numbers.extend(numbers)

    return jsonify(numbers=sorted(list(set(valid_numbers))))

if __name__ == 'main':
    app.run(host='0.0.0.0', port=8008)