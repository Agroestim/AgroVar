# Pulling python image from docker hub
FROM python:3.11.5-slim-bookworm

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD ab3135c2@
ENV DJANGO_SUPERUSER_EMAIL Giorgisprieto@outlook.com.ar

# Install service dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy proyect
COPY . .

# Set workdir directory
WORKDIR /app

# Run migrations
RUN python manage.py migrate
RUN python manage.py migrate api
# RUN python manage.py makemigrations

# Run collect statics
RUN python manage.py collectstatic

# Create superuser
RUN python manage.py createsuperuser --no-input --username admin-root

# Expose 
EXPOSE 8000
# Define the container entrypoint
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
