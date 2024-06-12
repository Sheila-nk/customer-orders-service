FROM python:3.11-slim

COPY . /customer-orders-service

WORKDIR /customer-orders-service

RUN pip install -r requirements.txt --default-timeout=100

ENV FLASK_APP=run.py

EXPOSE 8000

RUN ["chmod", "+x", "./commands.sh"]

ENTRYPOINT ["./commands.sh"]