# pull official base image
FROM python:3.11.4-slim-buster

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# set working directory
WORKDIR /usr/src/api

# set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./api/requirements/base.txt .
RUN pip install -r base.txt --no-cache-dir

# Expose port 8000 for web traffic
EXPOSE 8000

# Copy entrypoint script
COPY ./api/entrypoint.sh /usr/src/api/entrypoint.sh
RUN chmod +x /usr/src/api/entrypoint.sh

# Command to run entrypoint using entrypoint.sh script
CMD ["/usr/src/api/entrypoint.sh"]
