FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

RUN pip install -r requirements.txt

RUN cp ./app/config.temp.py /app/config.py 
