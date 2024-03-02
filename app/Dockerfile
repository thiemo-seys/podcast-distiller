FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ARG port
EXPOSE $port

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:$port"]
