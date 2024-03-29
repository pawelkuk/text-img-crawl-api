FROM python:3-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./manage.py"]