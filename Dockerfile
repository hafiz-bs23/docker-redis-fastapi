FROM python:3.11-alpine as api-setup

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./web /code/web
RUN pytest

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]

FROM nginx
COPY --from=api-setup /code/web /usr/share/nginx/html