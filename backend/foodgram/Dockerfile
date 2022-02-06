FROM python:3.7-slim

WORKDIR /app

COPY /requirements.txt /

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip3 install -r /requirements.txt --no-cache-dir

COPY foodgram/ /


CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]