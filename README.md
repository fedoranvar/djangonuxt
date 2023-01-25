<!-- docker-compose -f .docker/shell.yml run  web  django-admin startproject aplc -->
docker-compose run  --no-deps web  django-admin startproject config
docker-compose run  --no-deps web  sh -c "cd aplc;python manage.py startapp myfurst"
