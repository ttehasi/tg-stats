PORT ?= 8000
migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

dev:
	uv run python manage.py runserver

prod-run:
	uv run gunicorn -b 0.0.0.0:$(PORT) config.wsgi