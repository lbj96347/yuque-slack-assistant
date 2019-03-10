FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

COPY ./app/config.temp.py /app/config.py 

RUN pip install -r requirements.txt

