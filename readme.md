# Base Django Rest Framework Project

This is a base project that can be used when starting a new django rest framework project.

## To run with Docker
All you need is to run the following command:
```
docker-compose -f docker-compose.prod.yml up -d --build
```

Then run the migrations:
```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

Lastly for static files run collectstatic command:
```
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

To stop runnning containers:
```
docker-compose -f docker-compose.prod.yml down -v
```

## To run with virtual environment:
First, a virtual environment must be created and activated:
```
python3 -m venv env
source env/bin/activate
```

Then, all the requirements should be instaled:
```
pip install -r requirements.txt
```

And run the server:
```
python3 manage.py runserver
```
