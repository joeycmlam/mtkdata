FROM python:3

COPY . /src

WORKDIR /src


#RUN pip install pprint

RUN pip install yfinance

RUN pip install flask
RUN pip install Flask_restful
RUN pip install flask_cors

RUN pip install yfinance --upgrade --no-cache-dir

CMD [ "python", "./src/restcontrol.py" ]