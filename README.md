# Foodgram - Grocery Assistant (API)
![example workflow](https://github.com/Shchegolyaev/foodgram-project-react/actions/workflows/main.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

On this service, users will be able to publish recipes, subscribe to publications of other users, add favorite recipes to the "Favorites" list, and before going to the store, download a summary list of products needed to prepare one or more selected dishes.

## Project deployed:
The project is hosted in 4 containers (backend, frontend, postgres, nginx) on 
an Ubuntu virtual machine on the Yandex Cloud service.
<code>[foodhelper.ddns.net/recipes](http://foodhelper.ddns.net/recipes)
</code>
``````

Admin account:
```sh
* username: administrator
* password: admin
```

User account:
```
* email: test@test.ru
* password: Test1111
```

## Set up ci/cd:
* Test on flake8
* Build and push to DockerHub
* Push and deploy to server
* Send message to telegram (if successfully)


## Requirements:
* docker-compose
* docker
* nginx
* postgres

## How install (local):

* Replace to directory with ```dockerfile-compose.yaml```
* Run command:```docker-compose up```
* Project available on ```localhost```





## Contact
```sh
email: shchegolyaev.sergey@gmail.com

telegram: @shchegolyaev
```