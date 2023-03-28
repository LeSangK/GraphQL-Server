# local 環境の設定
TARGET := local
PROJECT_NAME := python-server

build:
	docker build -t $(PROJECT_NAME):$(TARGET) .

run:
	docker run --name $(PROJECT_NAME) --rm -p 8000:8000 $(PROJECT_NAME):$(TARGET)

install:
	pip3 install -r requirements.txt && pip3 freeze > requirements.lock