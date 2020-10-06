# Educa
Платформа для онлайн-обучения с собственной системой управления содержимым (Content Management System, CMS).


### Основной функционал:
- регистрация на платформе обучения как студент или как преподаватель;
- для преводавателей доступно добавление своих курсов и разделение их на модули;
- курсы могут содержать текст, видео, фото и прикрепленные файлы;
- студенты могут подписываться на курсы и проходить обучнение на платформе;
- настроено `REST Api` для просмотра списка курсов и студентов, запись на курсы;
- настроено кеширование с помощью `Memcached`.

## Установка
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Запуск проекта (на примере Linux)

Перед тем, как начать: если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

- Создайте на своем компютере папку проекта `mkdir educa` и перейдите в нее `cd educa`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/SergePogorelov/educa.git .`
- Создайте виртуальное окружение `python3 -m venv venv`
- Установите зависимости `pip install -r requirements.txt`
- Накатите миграции `python manage.py migrate`
- Создайте суперпользователя Django `python manage.py createsuperuser --username admin --email 'admin@example.com'`
- Запустите сервер разработки Django `python manage.py runserver`

## В разработке использованы

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Memcached](https://www.memcached.org/)
