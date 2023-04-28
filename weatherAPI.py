from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def get_weather():
    
    LATITUDE = request.args.get("lat")
    LONGITUDE = request.args.get("lon")
    KEY = "a6df1754733f5fef4256026cf2921a3c"
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={KEY}&units=metric'
    response = requests.get(url)
    file_content = response.content
    return file_content

if __name__ == '__main__':
    app.run()