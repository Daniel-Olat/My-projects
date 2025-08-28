from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
API_KEY = "3fd48da3d761c06e4a298994bc98c190"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "city not found"}), 404

    data = response.json()

    return jsonify({
        "city": data["name"],
        "temperature": data['main']['temp'],
        "description": data["weather"][0]['description'],
        "humidity": data['main']['humidity']
    })

if __name__ == "__main__":
    app.run(debug=True)