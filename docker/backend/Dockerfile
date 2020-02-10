FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install -U pip-tools
COPY . /code/
COPY ./docker/backend/entrypoint.sh /entrypoint.sh
WORKDIR /code/management_system
ENTRYPOINT [ "/entrypoint.sh" ]
