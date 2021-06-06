# NOTES

## Локальный запуск

1. Склонировать проект:

   ```bash
   git clone https://github.com/s0ul701/content.git
   ```

2. Зайти в папку проекта:

    ```bash
    cd content
    ```

3. Собрать Docker-образы:

    ```bash
    docker-compose build
    ```

4. Накатить миграции:

    ```bash
    docker-compose run server ./manage.py migrate
    ```

5. Запустить Docker-образы (+ скачать образы используемых сервисов):

    ```bash
    docker-compose up
    ```

6. Создать пользователя админки:

    ```bash
    docker-compose run server ./manage.py createsuperuser
    ```

## Справка по API

1. Получение списка Страниц [http://0.0.0.0:8000/api/v1/pages/](http://0.0.0.0:8000/api/v1/pages/)
2. Получение детальной информации о Странице [http://0.0.0.0:8000/api/v1/pages/{id}](http://0.0.0.0:8000/api/v1/pages/{id})
