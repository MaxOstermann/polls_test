# polls_test
Для запуска проекта через docker-compose:

1) Собираем командой:
sudo docker-compose build (все команды из корневой директории)
2) Запускаем:
sudo docker-compose up -d
3) Создаём пользователя
sudo docker-compose exec web python manage.py createsuperuser
4) запросы работают с авторизацией по токену - чтобы его получить, надо послать запрос на *hostname*/polls/api-token-auth/ вида:
{"username": *username*, "password": *password*}
5) Полученный токен используем в запросах с помощью заголовка 'Authorization: Token *token*'
6) Для запуска на локальной машине ставьте Debug=True для доступа к статике    

Автодокументацию по запросам можно найти на *hostname*/polls/ GET запросом (например, через браузер)
