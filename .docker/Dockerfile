FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ADD .docker/dev /usr/local/bin/
RUN ["chmod", "+x", "/usr/local/bin/dev"]
