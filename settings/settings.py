"""
All of settings information of this Rest API project will hold here
Created at: 28-07-2018
"""
__author__ = " Vubon Roy"

import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read environment variables
env = environ.Env(
    ALLOWED_HOSTS=(list),
)
envfile_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(envfile_path)

# ALLow hosts
ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Database settings

DATABASE = {
    "dbname": env('DATABASE_NAME'),
    "user": env('DATABASE_USERNAME'),
    "password": env('DATABASE_PASSWORD'),
    "host": env('DATABASE_HOST'),
    "port": env('DATABASE_PORT')
}

# end Database settings
