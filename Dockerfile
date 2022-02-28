FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt
COPY ./params.yaml /params.yaml

RUN pip install -r requirements.txt

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

COPY ./app /app
COPY ./models /models

CMD ["./start.sh"]