FROM python:3.10-slim-buster

WORKDIR /app
COPY . .

# Flask app port
EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "--app", "main", "run", "--host=0.0.0.0"]


