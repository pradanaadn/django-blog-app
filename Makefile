dev:
	uv run python manage.py runserver
shell :
	uv run python manage.py shell
migrate:
	uv run python manage.py migrate
model:
	uv run python manage.py makemigrations $(app)
apps:
	uv run python manage.py startapp $(app)
create_user:
	uv run python manage.py createsuperuser