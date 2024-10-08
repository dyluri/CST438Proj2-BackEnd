# Base Image
FROM python:3.12

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8888
ENV DEBUG=0

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        default-libmysqlclient-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Upgrade pip
RUN pip3 install --upgrade pip

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install project dependencies from requirements.txt
RUN pip install -r requirements.txt

CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT