# Base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Run the Django application
CMD ["gunicorn", "salonmanagement.wsgi:application", "--bind", "0.0.0.0:8000"]
