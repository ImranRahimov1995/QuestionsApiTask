python3 manage.py makemigrations --no-input
python3 manage.py migrate
python3 manage.py collectstatic --noinput

python3 manage.py loaddata fixtures/admin-user.json

exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload