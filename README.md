# QuestionsApiTask
Тестовое задание.
__________________________________________
## *Задача: спроектировать и разработать API для системы опросов пользователей.*
________________________________________________________
### Инструкция по развертованию .

1. git clone 
2. Заходите в docker-compose.yaml если нужно изменить окружение . есть две настройки окружение : local с включенным renderbrowsableApi, и Sqlite3.
Есть также prod настройки c jsonrender, postgres.

4. docker-compose build
5. docker-compose up 
___________________________________
### Документация по приминению ,примеры :

Функционал для администратора системы: 

1. авторизация в системе

##### /auth/login/

##### admin

##### 123

________________________________________________________
2.  добавление/изменение/удаление опросов. 
 
#### Создание опроса

*POST* /create/quiz/

{

    "title": "example_name",
    "end_date": "2021-12-29",
    "description": "some example description"
    
}
________________________________________________________
#### Получение/изменение/удоление  опроса

*GET|PUT|DELETE|* /get/<str: title>/ <------ title - это имя опроса *title*

 /get/example_name/
 
 {
 
    "id": 5,
    "title": "example_name",
    "start_date": "2021-12-15T22:33:19.525566Z",
    "end_date": "2021-12-29",
    "description": "some example descriptions"
    
}


________________________________________________________

#### Создание вопроса в опросе

*POST*  create/<str:quiz>/question/          <------ quiz - это имя опроса *title*

*POST*  create/example_name/question/

*можно отправить одно поле multiple_options , отправить пустой multiple_options, и с несколькоми вариантами.*

{

    "body":"Example question text s?",

    "multiple_options":{"first":"1","second":"2","third":"3","fourth":"4","fifth":"5"}

}

_____________________________________________________________________

#### Изменение вопроса в опросе

*GET|PUT|DELETE|*   get/str:quiz/pk/  <------ quiz - это имя опроса *title*  , pk - это id вопроса

/get/example_name/10/
 ________________________________________________________________________
### Пользовательский функционал (Пользователь может быть аутентифицирован или же быть анонимным )

####  Получение всех активныхх опросов

/quiz/all/
______________________________________________
####  Получение всех вопросов в опросе 

/quiz/<str:title>/  <------ title - это имя опроса *title*

/quiz/example_name/
_______________________________________________
#### Создание ответа на вопрос

*POST* /quiz/pk/create/answer/   <------ quiz - это имя опроса *title* , pk - это Id вопроса

/example_name/10/create/answer/
                                            
                                            
{
   
    "selected": "20",
    "second_selected": "",
    "third_selected": "",
                                            
}       

_____________________________________
#### Просмотр ответов в опросе конкретного пользователя

/user_id/quiz/answers/  <------ quiz - это имя опроса *title* , pk - это Id Пользователя

/1/example_name/answers/

_____________________________________
#### Просмотр всех ответов в опросе

/quiz/answers/ quiz - это имя опроса *title* ,

/example_name/answers/

                                                  
                                                  
                                                  
                                                  
