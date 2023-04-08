# Use the official Python image as the base image
FROM ubuntu:latest

# MySQLコネクターのインストール
RUN apt-get update && \
    apt-get install -y mysql-server && \
    apt-get install -y default-libmysqlclient-dev && \
    apt-get install -y python3 python3-pip && \
    pip install mysql-connector-python

# 環境変数の設定
ENV MYSQL_ROOT_PASSWORD=190727
ENV MYSQL_DATABASE=my_database_test

# データベースの初期化用スクリプトの配置
COPY init.sql /docker-entrypoint-initdb.d/

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the application
EXPOSE 8000

# Start the application
CMD ["python3", "run.py"]
