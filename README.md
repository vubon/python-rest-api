## A simple Rest API by Python 
I build a very basic rest api with Python. 

### How to use?
You can use it in virtualenv or docker. 

If you want to use virtualenv. Follow bellow instructions 

#### Virtualenv method

1. Create your virtualenv and activate your virtualenv install all libs from requirements.txt by below command

```bash
pip install -r requirements.txt 
```
2. Now create .env file in your root directory and add bellow text or strings 
```code
ALLOWED_HOSTS=*,127.0.0.1,
DATABASE_NAME=<your database name>
DATABASE_USERNAME=<your database username>
DATABASE_PASSWORD=<your datababse password>
DATABASE_HOST=<your database host>
DATABASE_PORT=5432
```
[N.B: You need to install postgresql database in your machine otherwise you can't use this project.]

3. After DB setup you need to run below command for creating tables in your DB. 

```bash
python db_table_creation.py
```
Don't forget to activate your virtualenv and also this command will work in your project root directory.

[N.B. Currently I was using RAW SQL for creating table , query data from DB. In future I have plan to move more Pythonic way, 
Making model, Migration and also I will implement ORM ]

4. Current project has static URLs. i.e Currently URL patten is not prefect. Below URLs are available only 

##### Recipes

| Name   | Method      | URL                    | Protected |
| ---    | ---         | ---                    | ---       |
| List   | `GET`       | `/recipes`             | ✘         |
| Create | `POST`      | `/recipes`             | ✓         |
| Get    | `GET`       | `/recipes/{id}`        | ✘         |
| Update | `PUT/PATCH` | `/recipes/{id}`        | ✓         |
| Delete | `DELETE`    | `/recipes/{id}`        | ✓         |
| Rate   | `POST`      | `/recipes/{id}/rating` | ✘         |

5. For accessing protected URLs you need to use basic authentication in your client(e.g. Postman) and use bellow credentials
```text
username: vubon
password: 123456

``` 
if you want to change. Go to servers folder and open default_user.py file . Find ususer_data function end of the file and change username and password too

6. That's all . 

#### Docker Method

1. Install Docker in your machine. My docker version was 18.06.0-ce and docker compose version 1.22.0
2. Use same version docker and docker compose . Unless the docker-compose.yml file configuration maybe mismatch 
3. Follow step 2 of virtualenv method. Now open docker-compose.yml file and go to postgres section. Use this DB name, DB username , DB password in your .env file.
remember that your database host is **postgres** .

4. Once you have done step 3. run bellow command 
```bash
[sudo] docker-compose up --build 
```
5. Only you need to build first time unless don't need . 
```bash
[sudo] docker-compose up
```
[N.B. Remember if you change anything in docker-compose file or Dockerfile you need to build and also if you add new libs in your project]
6. Follow step 4 of virtualenv for accessing URLs
7. If you want to change username and password follow step 5 of virtualenv method



### Credits**
I adopted many philosophies form **Django** in this project.

Thank you **Django Team** 

### Happy Coding 


