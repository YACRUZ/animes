FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /anime
WORKDIR /anime
COPY requirements.txt /anime/
RUN pip install -r requirements.txt
COPY . /anime/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080