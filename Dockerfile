# Pulling python image from docker hub
FROM python:3.11.5-slim-bookworm

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD ab3135c2@

# Install service dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy proyect
COPY . .

# Pulling python slim image from docker hub
# FROM python:3.11.5-slim-bookworm

# Set workdir directory
WORKDIR /app

# Copy from builder
# COPY --from=builder /app /app

# Run migrations
RUN python manage.py migrate
RUN python manage.py migrate api
# RUN python manage.py makemigrations

# Run collect statics
RUN python manage.py collecstatics

# Create superuser
RUN python manage.py createsuperuser --no-input --username root-admin --email Giorgisprieto@outlook.com.ar


# Expose and redirect ports
EXPOSE 8080

# Define the container entrypoint
ENTRYPOINT [ "python", "manage.py", "runserver", "localhost:8080" ]
