# QuestionsApiTask
Тестовое задание.
__________________________________________
## *Задача: спроектировать и разработать API для системы опросов пользователей.*
________________________________________________________
### Документация по приминению ,примеры :

Функционал для администратора системы:

1. авторизация в системе

##### /auth/login/

2.  добавление/изменение/удаление опросов. 
 
#### Создание опроса

*POST* /create/quiz/

{
    "title": "example_name",
    "end_date": "2021-12-29",
    "description": "some example description"
}

#### Создание вопроса в опросе

*POST*  create/<str:quiz>/question/          <------ quiz - это имя опроса *title*

*POST*  create/example_name/question/

можно отправить одно поле multiple_options , отправить пустой multiple_options, и с несколькоми вариантами.

{"body":"Example question text s?","multiple_options":{"first":"1","second":"2","third":"3","fourth":"4","fifth":"5"}}

