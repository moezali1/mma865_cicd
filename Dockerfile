FROM python:3.8-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["pytest", "test"]
