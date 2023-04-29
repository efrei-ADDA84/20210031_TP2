from flask import Flask
from flask import request
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_weather():
    
    LATITUDE = request.args.get("lat")
    LONGITUDE = request.args.get("lon")
    KEY = os.environ.get('API_KEY')

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={KEY}&units=metric'
    response = requests.get(url)
    file_content = response.content
    return file_content

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
