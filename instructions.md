
# Instructions



1. Install Python
```bash


sudo apt install python3 .  
```
2. Install a virtual enviroment



```bash
python3-pip python3-venv
```
3. install PostgreSQL.
```bash
sudo apt install postgresql postgresql-contrib
```
4. install Redis.
```bash
sudo apt-get install redis-server
```



5. Create virtual environment
```bash
python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```
6. Set up PSQL


```bash
postgres=# create database mydb;

postgres=# create user ceon with encrypted password '1235813f';

postgres=# grant all privileges on database mydb TO ceon ;
```
4. Django commands

```bash
python3 manage.py migrate

python3 manage.py makemigrations
```
5. Start app!
```bash
python3 manage.py runserver
```
The app running on port 8000
