<!-- docker-compose -f .docker/shell.yml run  web  django-admin startproject aplc -->
docker-compose run  --no-deps web  django-admin startproject config
sudo chown -R master:users app
docker-compose exec  web  sh -c "cd app;python manage.py createsuperuser"
docker-compose run  --no-deps web  sh -c "cd app;python manage.py startapp claims"

docker-compose exec  web  sh -c "cd app;python manage.py makemigrations"
docker-compose exec  web  sh -c "cd app;python manage.py migrate"
docker-compose exec  web  sh -c "cd app;python manage.py migrate createsuperuser"
