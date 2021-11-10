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

___going to add code from here
- [ ] User API
  - [ ] Get User Data
  - [ ] Edit User Data
  - [ ] Resign user
- [ ] Crawling API & Crawling Function
- [ ] Product API
    - [ ] Valid duplicate Product by Title
    - [ ] Get Product Data
