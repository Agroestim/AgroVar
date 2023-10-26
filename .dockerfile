# Pulling python image from docker hub
FROM python:3.11.5-bookworm as builder

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD ab3135c2@

# Install system dependencies
RUN apt-get update && apt-get install -y netcat

# Install service dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# Copy proyect
COPY . .

# Pulling python slim image from docker hub
FROM python:3.11.5-slim-bookworm

# Set workdir directory
WORKDIR /app

# Copy from builder
COPY --from=builder /app /app

# Run migrations
RUN python manage.py migrate
RUN python manage.py migrate api
RUN python manage.py makemigrations

# Run collect statics
RUN python manage.py collecstatics

# Create superuser
RUN python -m django createsuperuser --username root-admin



# Expose and redirect ports
EXPOSE 8080-80

# Define the container entrypoint
ENTRYPOINT [ "python", "manage.py", "runserver", "" ]
