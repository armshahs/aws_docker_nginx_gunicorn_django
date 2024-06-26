# Use a slim python image as the base
FROM python:3.11-slim

# To view logs in terminal:
#ENV PYTHONUNBUFFERED=1

# Set a working directory for the container
WORKDIR /app

# Copy local app
COPY ./aws_docker_nginx_gunicorn_django ./

# Install dependencies
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir


# Run gunicorn as the main process
CMD [ "gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000"]
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
