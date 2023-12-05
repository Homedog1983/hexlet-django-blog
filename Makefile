install:
	poetry install
lint:
	poetry run flake8 hexlet_django_blog
dev:
	python3 manage.py runserver
