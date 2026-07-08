FROM python:3.14

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "StoreApp.wsgi:application"]