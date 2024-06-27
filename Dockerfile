# Use a slim python image as the base
FROM python:3.11-slim


# ENVs -----------
# disables the version check for pip for better performance & not cluttering the CI/CD pipeline
# ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# prevents Python from writing .pyc files to reduce storage & improve performance 
# ENV PYTHONDONTWRITEBYTECODE 1

# To view logs real-time in terminal:
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
