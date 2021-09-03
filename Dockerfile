FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile
COPY . /code/
RUN pipenv run python manage.py migrate

EXPOSE 8000

CMD [ "pipenv", "run", "gunicorn", "fines.wsgi" ]
