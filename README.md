# Teacher Portal

## Setup Instructions

1. Clone the repo:

git clone https://github.com/Thamu123/teacher-portal.git
cd teacher-portal

## Create a Virtual Env
python -m venv venv
source venv/bin/activate  
# if Windows: venv\Scripts\activate

# Run this command for installing dependencies
pip install -r requirements.txt

# Migration
python manage.py makemigrations
python manage.py migrate

# Enter email, name, password when prompted to create the user
python manage.py create_teacher

## Enter this command for creating sample 20 students
python manage.py create_students

## Then finally run the server
python manage.py runserver

    -- load to your localhost

### You can test also
pytest




