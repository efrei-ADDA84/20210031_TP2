FROM python:3.8.10
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8081
CMD [ "python", "weatherAPI.py" ]