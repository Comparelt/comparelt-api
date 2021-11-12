# Comparelt API Server with Flask & PostgreSQL & BeautifulSoup4

## How to run
    pip install -r requirements.txt
    
    flask db init    
    flask db migrate // Only for first time
    flask db upgrade // After migrate 
    
    flask run

## Description Detail
Refactored Every Part to MVC ( Model, View, Controller ) Pattern.  

Enter api directory and there will be 4 directories which is Auth(Login / SignUo Part),   
Crawling, Product, User, test, and __ _init_ __.py, app.py. 

- app.py: Run API Server code is added in here.
- api /__init __.py: DataBase models imported on here.
  
In User, and Product directory, there are models.py, service.py, controller.py  
- models.py: DataBase ORM code is added in here.
- service.py: API Logic code is added in here.
- controller.py: API endPoint is import in here.

Other directories( Auth, Crawling ) use model of User, and Product.  
So they shouldn't have models.py

test / test.py is unittest code for checking API function.



## TODO List

- [X] Link Flask with PostgreSQL
- [x] Product DataBase Model
- [x] User DataBase Model
- [x] Auth(Login / SignUp) API
- [ ] User API
  - [ ] Get User Data
  - Get User Data means if the frontend request to backend about user's data with user id, the          backend will find user in database with the given user id. And if there is the same id in            database, the server will return found user's data to frontend by json type like { id: 1,             username: 'Han', email:"dku@dku.com", etc }.
  - [ ] Edit User Data
  - Edit User data means for example, If i edit my username from 'Han' to 'HyunTaek' in frontend, the     frontend will send request to backend with user data in json type with the changed username           like {id: 1, username: 'HyunTaek', email:"dku@dku.com", etc }. And the backend will update           user by first finding the user from database with id in given json data. With the found user,         the backend will update all the data given.
  - [x] Resign user
- [x] Crawling API & Crawling Function
- [ ] Product API
    - [ ] Valid duplicate Product by Title
    - Valid duplicate doesn't include crawling. It will just return true or false
    - [ ] Get Product Data
    - Returns Product data from the database to the front end
   
