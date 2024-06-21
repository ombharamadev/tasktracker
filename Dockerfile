# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY req.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Run migrations and other setup commands
RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

# Expose the port the application runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
