CREATE USER admin WITH PASSWORD 'devpass';
CREATE DATABASE app_db;
GRANT ALL PRIVILEGES ON DATABASE app_db TO admin;