#!/bin/bash

until mysqladmin ping -h db --silent; do
  echo 'waiting for mysqld to be connectable...'
  sleep 2
done

echo "go app is started!"
python3 -u main.py