FROM python:3.12.1
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /app/
CMD ["/bin/sh", "-c", "python3 manage.py makemigrations --noinput && python3 manage.py migrate --noinput && python3 manage.py collectstatic --noinput && gunicorn user.wsgi:application --bind 0.0.0.0:8000"]
