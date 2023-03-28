# Use the official Python image as the base image
FROM python:3.9

# ベースイメージの指定
FROM mysql:8.0

# 環境変数の設定
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=my_database_test
ENV MYSQL_USER=sou.raku
ENV MYSQL_PASSWORD=Rcm_1907

# MySQLコネクターのインストール
RUN apt-get update && \
    apt-get install -y python3-dev default-libmysqlclient-dev build-essential && \
    pip install mysql-connector-python==8.0.22

# データベースの初期化用スクリプトの配置
COPY init.sql /docker-entrypoint-initdb.d/

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the application
EXPOSE 8000

# Start the application
CMD ["python", "run.py"]