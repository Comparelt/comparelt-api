.ONESHELL:

.PHONY: clean pip-packages install tests init migrate upgrade run first

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

pip-packages:
	sudo apt install python-pip -y

install:
	pip3 install -r requirements.txt;

tests:
	python3 main.py test

init:
	python3 main.py db init

migrate:
	python3 main.py db migrate

upgrade:
	python3 main.py db upgrade

run:
	python3 main.py run

first: clean pip-packages install init migrate run