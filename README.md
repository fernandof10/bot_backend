# The Bot_backend

This project consist of a HTTP/REST backend 

## Requirements

The backend will have two resources:

 - `/bots`: the bot resource represent the bots registered in our Bot platform. The /bots
endpoint have to manage all operations related to bots i.e. create, read, update and delete.

e.g.:
```
- POST /bots
{
"id": "123456-789-123-123-7812546",
"name": "Alpha"
} -
GET /bots/:id
{
"id": "asd41464-4564asd-454adc8-vtynv-4556",
"name": "Bravo"
}
```

- `/messages`: a bot exchange messages with users. All users are considered anonymous in our
platform -- hence they don't need to be registered nor logged in. Nevertheless, users'
session are represented by an unique id. It can be either the from or the to attribute in a
message, depending on whether he received or sent it.
All the messages exchanged between a bot and an user, during a conversation, will be
correlated by a conversationId. The API should be capable of: 
1. registering new messages for a given conversation
2. return a message by its id
3. return all messages of a given conversation. Messages won't be updated nor deleted.

e.g.:
```
- POST /messages
{
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:52.6917722Z",
"from": "36b9f842-ee97-11e8-9443-0242ac120002",
"to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"text": "Oi! Como posso te ajudar?"
}
- GET /messages/:id
{
"id": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:52.6917722Z",
"from": "36b9f842-ee97-11e8-9443-0242ac120002",
"to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"text": "Oi! Como posso te ajudar?"
}
- GET /messages?conversationId=:conversationId
[
{
"id": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:52.6917722Z",
"from": "36b9f842-ee97-11e8-9443-0242ac120002",
"to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"text": "Oi! Como posso te ajudar?"
},
{
"id": "67ade836-ea2e-4992-a7c2-f04b696dc9ff",
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:57.5926721Z",
"from": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"to": "36b9f842-ee97-11e8-9443-0242ac120002",
"text": "Gostaria de saber meu resultado do exame?"
}
]
```

## Implementation

### Overview
During the development of `The Bot_backend` I will use an adapted agile methodology, considering that this is a demo project, with just one person acting as Scrum Master, Product Owner and Developer. The idea is to delivery at least a Minimum Viable Product (MVP) by today. If there is time, I will start run new development cycle (adding features, testing and deploying).


Considering that this project demands quick development, I chose the following points:

- Programing language: `Python`
- Framework: `Flask`
- Database: In the first development cycle I will use `SQLite` database, good for small applications, with few users accessing them which makes it well suited to demonstrate how the project works. If I have time, in the next development cycle (cycle 2) I will add the option to use a `MySQL` database, which is good for applications that demands higher security/authentication , multiple users reading/writing data.

### Main activities
I created the dashboard below using Trello with the main backlogs to develop considering the developments cycles 1 and 2. By the deadline of this challenge, I intend finish at least the backlogs tagged as Cycle 1.

![backlogs](/images/initial_scrum_board.jpg)

### Macro overview about the implementation

I created the high level/conceptual UML class diagram to guide me during the development.
As the image shows, the idea it to have a `BotsAPI` which will handle all HTTP/backend functions to add, update, delete and get the bots and messages withing flask framework. It will also communicate 
with `DataBase` interface, which is responsible to access, retrieve and insert data into the database.
As I foresee a possibility to use different kinds of databases (SQLite, MySQL or any other one), I used the `Factory Method` design pattern, which makes this generalization possible. That is why there are two other concrete classes in the diagram (`SQLiteDatabaseInterface` and `MySQLDataBaseInterface`).

The multiple clients requests are represented by `ClientApiRequests`, containing the messages that the customer sends or receive. It is responsible to assign unique ids for the customers, conversation, and bots. As it is not the focus of the project, I will use pre-defined values for the IDs.

![conceptual_diagram](/images/conceptual_diagram.jpg)

### Implementation result

By the end of this challenge I could develop a prototype for `The Bot Backend`, investing around 12 hours to plan, develop and test. I think I achieved the goal to develop a MVP application that at least for demonstration is OK. The tests results are in the `Test Results` section.
If I had more time, it would be desirable:
- Refactor the code (as part of agile methodology) to handle better errors, check input type and format,
add more comments and annotations.
- Design much more test cases (black and white box tests), in order to stress the application with more scenarios
- In a second development cycle, include MySQL database
- Document better the application (draw UML diagrams, flowcharts etc) and how to use it
- Add a feature to generate the message_id and timestamp in the example format

Almost all backlogs related to cycle 1 in the dashboard are completed:

![backlogs_end](/images/final_scrum_board.jpg)

## How to run the project

- clone the project to your computer
- ensure you have python3 installed
- enrure the python modules imported in `data_base_interfaces.py` and `bots_api.py` are installed
- Case you don't have flask installed, run `pip install Flask`
- go to the project directory using `cd the_bot_api`
- execute the command `export FLASK_APP=bots_api.py`
- execute `export FLASK_ENV=development` case you want to work in the project
- execute `flask run`
- run the curl commands (GET, POST, DELETE, PUT) as I used in the `Test Results` section


## Test Results

- POST/bots
```console
$ curl -i -H  "Content-Type: application/json"  -X POST -d '{"id":"77b9f842-ee97-11e8-9443-0242ac120002", "name": "Bravo"}' http://127.0.0.1:5000/bots
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   160  100    98  100    62   1507    953 --:--:-- --:--:-- --:--:--  2500
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 98
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:18:51 GMT

{
  "bot": {
    "bot_id": "77b9f842-ee97-11e8-9443-0242ac120002",
    "bot_name": "Bravo"
  }
}
```

```console
$ curl -i -H  "Content-Type: application/json"  -X POST -d '{"id":"36b9f842-ee97-11e8-9443-0242ac120002", "name": "Charles"}' http://127.0.0.1:5000/bots
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   160  100    98  100    62    222    140 --:--:-- --:--:-- --:--:--   364
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 98
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:18:42 GMT

{
  "bot": {
    "bot_id": "36b9f842-ee97-11e8-9443-0242ac120002",
    "bot_name": "Charles"
  }
}
```

- GET /bots
```console
$ curl -i http://localhost:5000/bots
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   196  100   196    0     0    920      0 --:--:-- --:--:-- --:--:--   920
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 196
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:28:11 GMT

{
  "bots": [
    {
      "id": "36b9f842-ee97-11e8-9443-0242ac120002",
      "name": "Charles"
    },
    {
      "id": "77b9f842-ee97-11e8-9443-0242ac120002",
      "name": "Bravo"
    }
  ]
}
```

- GET /bots/:id
```console
$ curl -i http://localhost:5000/bots/36b9f842-ee97-11e8-9443-0242ac120002
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    90  100    90    0     0    400      0 --:--:-- --:--:-- --:--:--   400
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 90
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:27:46 GMT

{
  "bot": {
    "id": "36b9f842-ee97-11e8-9443-0242ac120002",
    "name": "Charles"
  }
}
```

- PUT /bots/id
```console
$ curl -i -H  "Content-Type: application/json"  -X PUT -d '{"id":"36b9f842-ee97-11e8-9443-0242ac120002", "name": "ACharles"}' http://127.0.0.1:5000/bots/36b9f842-ee97-11e8-9443-0242ac120002
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    91  100    28  100    63     66    148 --:--:-- --:--:-- --:--:--   215
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:32:11 GMT

{
  "update_sucess": true
}
```

- DELETE bots/id
```console
$ curl -i -H  "Content-Type: application/json"  -X DELETE -d '{"id":"36b9f842-ee97-11e8-9443-0242ac120002"}' http://127.0.0.1:5000/bots/36b9f842-ee97-11e8-9443-0242ac120002
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    66  100    21  100    45     48    104 --:--:-- --:--:-- --:--:--   153
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:37:00 GMT

{
  "result": true
}
```

- POST /messages
```console
$ curl -i -H  "Content-Type: application/json"  -X POST -d '{"id": "16edd3b3-3f75-40df-af07-2a3813a79ce9", "conversationId":"7665ada8-3448-4acd-a1b7-d688e68fe9a1", "timestamp": "2018-11-16T23:30:52.6917722Z", "from": "36b9f842-ee97-11e8-9443-0242ac120002", "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9", "text": "Oi! Como posso te ajudar?"}' http://127.0.0.1:5000/messages
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   530  100   251  100   279    607    675 --:--:-- --:--:-- --:--:--  1286
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 251
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:38:18 GMT

{
  "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
  "from": "36b9f842-ee97-11e8-9443-0242ac120002",
  "text": "Oi! Como posso te ajudar?",
  "timestamp": "2018-11-16T23:30:52.6917722Z",
  "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9"
}
```

```console
$ curl -i -H  "Content-Type: application/json"  -X POST -d '{"id": "67ade836-ea2e-4992-a7c2-f04b696dc9ff", "conversationId":"7665ada8-3448-4acd-a1b7-d688e68fe9a1", "timestamp": "2018-11-16T23:30:57.5926721Z", "from": "16edd3b3-3f75-40df-af07-2a3813a79ce9", "to": "36b9f842-ee97-11e8-9443-0242ac120002", "text": "Gostaria de saber meu exame?"}' http://127.0.0.1:5000/messages
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   536  100   254  100   282    593    658 --:--:-- --:--:-- --:--:--  1252
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 254
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:42:03 GMT

{
  "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
  "from": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
  "text": "Gostaria de saber meu exame?",
  "timestamp": "2018-11-16T23:30:57.5926721Z",
  "to": "36b9f842-ee97-11e8-9443-0242ac120002"
}
```

- GET /messages?conversationId=:conversationId
```console
$ curl -i http://127.0.0.1:5000/messages?conversationId=7665ada8-3448-4acd-a1b7-d688e68fe9a1
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   693  100   693    0     0   169k      0 --:--:-- --:--:-- --:--:--  225k
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 693
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:46:57 GMT

{
  "messages": [
    {
      "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
      "from": "36b9f842-ee97-11e8-9443-0242ac120002",
      "id": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
      "text": "Oi! Como posso te ajudar?",
      "timestamp": "2018-11-16T23:30:52.6917722Z",
      "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9"
    },
    {
      "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
      "from": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
      "id": "67ade836-ea2e-4992-a7c2-f04b696dc9ff",
      "text": "Gostaria de saber meu exame?",
      "timestamp": "2018-11-16T23:30:57.5926721Z",
      "to": "36b9f842-ee97-11e8-9443-0242ac120002"
    }
  ]
}
```

- GET /messages/:id
```console
$ curl -i http://127.0.0.1:5000/messages/67ade836-ea2e-4992-a7c2-f04b696dc9ff
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   334  100   334    0     0  83500      0 --:--:-- --:--:-- --:--:--  108k
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 334
Server: Werkzeug/0.16.0 Python/3.7.4
Date: Sat, 22 Aug 2020 23:49:59 GMT

{
  "message": {
    "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
    "from": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
    "id": "67ade836-ea2e-4992-a7c2-f04b696dc9ff",
    "text": "Gostaria de saber meu exame?",
    "timestamp": "2018-11-16T23:30:57.5926721Z",
    "to": "36b9f842-ee97-11e8-9443-0242ac120002"
  }
}
```

- to test data_base_interfaces.py I executed the file as main and got the following result as expected

```console
$ python data_base_interfaces.py
True
Successfully updated bot 36b9f842-ee97-11e8-9443-0242ac120002, with the name Delta
[{'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Delta'}]
[{'id': '36b9f842-ee97-11e8-9443-0242ac120002', 'name': 'Delta'}]
Successfully deleted bot 36b9f842-ee97-11e8-9443-0242ac120002
True
[{'id': 'mid-1', 'conversationId': 'cid-1', 'timestamp': 'time1', 'from': 'f-1', 'to': 'to-1', 'text': 'text1'}]
[{'id': 'mid-1', 'conversationId': 'cid-1', 'timestamp': 'time1', 'from': 'f-1', 'to': 'to-1', 'text': 'text1'}]
```

- Screenshots from the SQLite database after running some curl commands

![screenshots](/images/example_messages_sqlite.JPG)
![screenshots](/images/example_bots_sqlite.JPG)