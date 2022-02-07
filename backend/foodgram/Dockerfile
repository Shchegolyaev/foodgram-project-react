FROM python:3.9

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY . .

RUN python manage.py makemigrations users
RUN python manage.py makemigrations recipes
RUN python manage.py migrate

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]