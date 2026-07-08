python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(
        '$DJANGO_SUPERUSER_USERNAME',
        '$DJANGO_SUPERUSER_EMAIL',
        '$DJANGO_SUPERUSER_PASSWORD'
    )
    print('Superuser created successfully')
else:
    print('Superuser already exists')
EOF

if [ "$DJANGO_ENV" = "production" ]; then
    gunicorn StoreApp.wsgi:application --bind 0.0.0.0:8000 --workers 3
else
    python manage.py runserver 0.0.0.0:8000
fi