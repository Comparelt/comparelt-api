# Comparelt API Server with Flask & PostgreSQL & BeautifulSoup4

## How to run with python
    > pip install -r requirements.txt
    
    > python main.py db init
    > python main.py db migrate // Only for first time
    > python main.py db upgrade // If you update db model 
    
    > python main.py run
## How to run with Makefile
    > make first

## How to Test
    > python main.py test

## Description Detail
Refactored Every Part to MVC ( Model, View, Controller ) Pattern.  

Enter api directory and there will be 2 directories which is main, test, and __ _init_ __.py.
main.py: Run API Server code is added in here.
- api /__init __.py: APIs are import on here.

In main/ , there are controller, model, service, util, __ init __.py, config.py.  

- main/ controller: Every API controller is in this directory.
- main/ model: Every ORM model is in this directory.
- main/ service: Every API logic(service) is in this directory.
- main/ util: dto & utility is in this directory.

api/ test is unittest directory for checking API function. (Login/SignUp Test)


## TODO List

- [X] Link Flask with PostgreSQL
- [x] Product DataBase Model
- [x] User DataBase Model
- [x] Auth(Login / SignUp) API
- [x] User API
  - [x] Get User Data
  - Get User Data means if the frontend request to backend about user's data with user id, the          backend will find user in database with the given user id. And if there is the same id in            database, the server will return found user's data to frontend by json type like { id: 1,             username: 'Han', email:"dku@dku.com", etc }.
  - [x] Edit User Data
  - Edit User data means for example, If i edit my username from 'Han' to 'HyunTaek' in frontend, the     frontend will send request to backend with user data in json type with the changed username           like {id: 1, username: 'HyunTaek', email:"dku@dku.com", etc }. And the backend will update           user by first finding the user from database with id in given json data. With the found user,         the backend will update all the data given.
  - [x] Resign user
- [x] Crawling API & Crawling Function
- [x] Product API
    - [x] Valid duplicate Product by Title
    - Valid duplicate doesn't include crawling. It will just return true or false
    - [x] Get Product Data
    - Returns Product data from the database to the front end
   
