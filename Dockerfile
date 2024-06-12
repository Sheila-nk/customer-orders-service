FROM python:3.11-slim

ARG USERNAME=myuser
ARG UID=1000
RUN adduser --disabled-password --gecos '' --uid $UID $USERNAME

COPY . /customer-orders-service

WORKDIR /customer-orders-service

RUN pip install --no-cache-dir -r requirements.txt --default-timeout=100

ENV FLASK_APP=run.py

RUN chown -R $USERNAME:$USERNAME /customer-orders-service

USER $USERNAME

EXPOSE 8000

RUN ["chmod", "+x", "./commands.sh"]

ENTRYPOINT ["./commands.sh"]