FROM python:3.7

RUN pip install --upgrade setuptools

COPY ./app /app
COPY ./models /models
COPY ./params.yaml /params.yaml
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./start.sh /start.sh
RUN chmod +x /start.sh


CMD ["./start.sh"]