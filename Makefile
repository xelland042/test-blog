mig:
	python manage.py makemigrations
	python manage.py migrate
run:
	python manage.py runserver 0.0.0.0:8000