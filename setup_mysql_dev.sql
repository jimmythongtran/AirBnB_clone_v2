-- this prepares a MySQL server for this project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVELEGES ON * . * hbnb_dev_db;

