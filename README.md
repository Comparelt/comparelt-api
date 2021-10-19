# Comparelt API Server with Flask & PostgreSQL & BeautifulSoup4

## How to run
    pip install -r requirements.txt
    
    flask db init    
    flask db migrate // Only for first time
    flask db upgrade // After migrate 
    
    Run api/app.py

## Description Detail

- app.py: API code is added in here.
- __init __.py: DataBase models imported on here. 
- models.py: DataBase ORM code is added in here.

## TODO List

- [X] Link Flask with PostgreSQL
- [x] Product DataBase Model
- [x] User DataBase Model
- [x] Auth(Login / SignUp) API
- [ ] User API
- [ ] Crawling API & Crawling Function
- [ ] Product API