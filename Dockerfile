FROM python:3.8.10
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "weather_wrapper.py" ]