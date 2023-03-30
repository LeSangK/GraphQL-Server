# local 環境の設定
TARGET := local
PROJECT_NAME := python-server

build:
	docker build -t $(PROJECT_NAME):$(TARGET) .

run:
	docker-compose up 

install:
	pip3 install -r requirements.txt && pip3 freeze > requirements.lock