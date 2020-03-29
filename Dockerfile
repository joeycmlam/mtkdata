FROM python:alpine3.7

COPY . /src

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python3 ./index.py