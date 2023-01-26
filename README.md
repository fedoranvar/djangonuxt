<!-- docker-compose -f .docker/shell.yml run  web  django-admin startproject aplc -->
docker-compose run  --no-deps backend  django-admin startproject config
sudo chown -R master:users backend
docker-compose exec  backend  sh -c "cd backend;python manage.py createsuperuser"
docker-compose run  --no-deps backend  sh -c "cd backend;python manage.py startbackend claims"

docker-compose exec  backend  sh -c "cd backend;python manage.py makemigrations"
docker-compose exec  backend  sh -c "cd backend;python manage.py migrate"
docker-compose exec  backend  sh -c "cd backend;python manage.py createsuperuser"


dc run frontend bash
