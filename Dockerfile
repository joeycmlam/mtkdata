FROM python:3

COPY . /src

WORKDIR /src



RUN pip install alpha_vantage

RUN pip install flask
RUN pip install Flask_restful
RUN pip install flask_cors



CMD [ "python", "./src/restcontrol.py" ]