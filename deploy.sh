# Activate virtual environment
if [[ "$VIRTUAL_ENV" = "" ]] then
    source .venv/bin/activate
fi

# Install requirements
pip install -r requirements.txt

# Run migrations and collect static files
python manage.py migrate
python manage.py collectstatic --noinput

# Start server
systemctl restart gunicorn.socket
systemctl reload nginx.service
